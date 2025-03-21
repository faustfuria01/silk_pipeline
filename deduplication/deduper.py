from typing import List

def deduplicate_hosts(hosts: List[dict]) -> List[dict]:
    """
    Deduplicates the host list by ip_address.
    If there are duplicates, the entry with the more recent last_seen is selected and the vendor list is merged.
    """
    deduped = {}
    for host in hosts:
        ip = host.get("ip_address")
        if ip in deduped:
            existing = deduped[ip]
            if host["last_seen"] > existing["last_seen"]:
                deduped[ip] = host
            # Combining supplier information
            vendors = set()
            if isinstance(existing.get("vendor"), list):
                vendors.update(existing["vendor"])
            else:
                vendors.add(existing.get("vendor"))
            if isinstance(host.get("vendor"), list):
                vendors.update(host["vendor"])
            else:
                vendors.add(host.get("vendor"))
            deduped[ip]["vendor"] = list(vendors)
        else:
            deduped[ip] = host
    return list(deduped.values())
