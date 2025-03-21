import aiohttp
import logging
from config import QUALYS_API_URL, API_KEY

logger = logging.getLogger(__name__)

class AsyncQualysClient:
    async def fetch_hosts(self) -> list:
        """
        Asynchronously receives host data from Qualys API.
        In case of an error, test data is returned.
        """
        headers = {"Authorization": f"Bearer {API_KEY}"}
        url = f"{QUALYS_API_URL}/hosts"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    response.raise_for_status()
                    data = await response.json()
                    logger.info("Fetched data from Qualys asynchronously")
                    return data
        except Exception as e:
            logger.error(f"Error fetching from Qualys API: {e}")
            return [
                {
                    "id": "q1",
                    "ip": "192.168.1.10",
                    "hostname": "host-qualys-1",
                    "os": "Windows",
                    "lastSeen": "2025-03-18T12:00:00"
                },
                {
                    "id": "q2",
                    "ip": "192.168.1.11",
                    "hostname": "host-qualys-2",
                    "os": "Linux",
                    "lastSeen": "2025-03-19T08:30:00"
                }
            ]
