import aiohttp
import logging
from config import CROWDSTRIKE_API_URL, API_KEY

logger = logging.getLogger(__name__)

class AsyncCrowdstrikeClient:
    async def fetch_hosts(self) -> list:
        """
        Asynchronously receives host data from Crowdstrike API.
        In case of an error, test data is returned.
        """
        headers = {"Authorization": f"Bearer {API_KEY}"}
        url = f"{CROWDSTRIKE_API_URL}/hosts"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    response.raise_for_status()
                    data = await response.json()
                    logger.info("Fetched data from Crowdstrike asynchronously")
                    return data
        except Exception as e:
            logger.error(f"Error fetching from Crowdstrike API: {e}")
            return [
                {
                    "uuid": "c1",
                    "ipAddress": "192.168.1.10",
                    "name": "host-crowdstrike-1",
                    "operating_system": "Windows 10",
                    "last_seen": "2025-03-17T15:45:00"
                },
                {
                    "uuid": "c2",
                    "ipAddress": "192.168.1.12",
                    "name": "host-crowdstrike-2",
                    "operating_system": "Ubuntu",
                    "last_seen": "2025-03-19T09:15:00"
                }
            ]
