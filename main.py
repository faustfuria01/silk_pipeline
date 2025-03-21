import os
import asyncio
import logging
from fetcher.async_qualys_client import AsyncQualysClient
from fetcher.async_crowdstrike_client import AsyncCrowdstrikeClient
from normalization.normalizer import normalize_qualys_host, normalize_crowdstrike_host
from deduplication.deduper import deduplicate_hosts
from db.mongodb_client import get_db
from visualization.charts import plot_os_distribution, plot_host_age
from logging_config import setup_logging


def save_hosts_to_db(hosts):
    db = get_db()
    hosts_collection = db["hosts"]
    hosts_collection.delete_many({})
    hosts_collection.insert_many(hosts)


async def fetch_all_hosts():
    qualys_client = AsyncQualysClient()
    crowd_client = AsyncCrowdstrikeClient()
    return await asyncio.gather(
        qualys_client.fetch_hosts(),
        crowd_client.fetch_hosts()
    )


async def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    if not os.path.exists("charts"):
        os.makedirs("charts")

    logger.info("Starting asynchronous data fetching...")
    raw_qualys, raw_crowdstrike = await fetch_all_hosts()

    logger.info(f"Fetched {len(raw_qualys)} hosts from Qualys")
    logger.info(f"Fetched {len(raw_crowdstrike)} hosts from Crowdstrike")

    normalized_hosts = []
    for host in raw_qualys:
        normalized_hosts.append(normalize_qualys_host(host))
    for host in raw_crowdstrike:
        normalized_hosts.append(normalize_crowdstrike_host(host))

    logger.info(f"Total normalized hosts: {len(normalized_hosts)}")

    deduped_hosts = deduplicate_hosts(normalized_hosts)
    logger.info(f"Total deduped hosts: {len(deduped_hosts)}")

    save_hosts_to_db(deduped_hosts)
    logger.info("Deduped hosts saved to MongoDB.")

    plot_os_distribution(deduped_hosts)
    plot_host_age(deduped_hosts)
    logger.info("Charts generated and saved in the 'charts' folder.")


if __name__ == "__main__":
    asyncio.run(main())
