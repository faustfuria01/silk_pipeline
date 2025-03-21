from datetime import datetime

def normalize_qualys_host(raw_host: dict) -> dict:
    """
    Normalizes host data from Qualys.
    """
    return {
        "vendor": "Qualys",
        "host_id": raw_host.get("id"),
        "ip_address": raw_host.get("ip"),
        "hostname": raw_host.get("hostname"),
        "os": raw_host.get("os"),
        "last_seen": datetime.fromisoformat(raw_host.get("lastSeen"))
    }

def normalize_crowdstrike_host(raw_host: dict) -> dict:
    """
    Normalizes host data from Crowdstrike.
    """
    return {
        "vendor": "Crowdstrike",
        "host_id": raw_host.get("uuid"),
        "ip_address": raw_host.get("ipAddress"),
        "hostname": raw_host.get("name"),
        "os": raw_host.get("operating_system"),
        "last_seen": datetime.fromisoformat(raw_host.get("last_seen"))
    }
