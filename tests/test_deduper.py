from datetime import datetime
from deduplication.deduper import deduplicate_hosts

def test_deduplication():
    hosts = [
        {"ip_address": "192.168.1.10", "last_seen": datetime(2025, 3, 18, 12, 0), "vendor": "Qualys"},
        {"ip_address": "192.168.1.10", "last_seen": datetime(2025, 3, 19, 9, 0), "vendor": "Crowdstrike"},
        {"ip_address": "192.168.1.11", "last_seen": datetime(2025, 3, 17, 12, 0), "vendor": "Qualys"},
    ]
    deduped = deduplicate_hosts(hosts)
    assert len(deduped) == 2
    for host in deduped:
        if host["ip_address"] == "192.168.1.10":
            assert host["last_seen"] == datetime(2025, 3, 19, 9, 0)
