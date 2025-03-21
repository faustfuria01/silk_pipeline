from datetime import datetime
from normalization.normalizer import normalize_qualys_host, normalize_crowdstrike_host

def test_normalize_qualys():
    raw = {
        "id": "q1",
        "ip": "192.168.1.10",
        "hostname": "test-host",
        "os": "Windows",
        "lastSeen": "2025-03-18T12:00:00"
    }
    norm = normalize_qualys_host(raw)
    assert norm["vendor"] == "Qualys"
    assert norm["host_id"] == "q1"
    assert norm["ip_address"] == "192.168.1.10"
    assert norm["hostname"] == "test-host"
    assert norm["os"] == "Windows"
    assert isinstance(norm["last_seen"], datetime)

def test_normalize_crowdstrike():
    raw = {
        "uuid": "c1",
        "ipAddress": "192.168.1.10",
        "name": "test-host",
        "operating_system": "Ubuntu",
        "last_seen": "2025-03-19T09:15:00"
    }
    norm = normalize_crowdstrike_host(raw)
    assert norm["vendor"] == "Crowdstrike"
    assert norm["host_id"] == "c1"
    assert norm["ip_address"] == "192.168.1.10"
    assert norm["hostname"] == "test-host"
    assert norm["os"] == "Ubuntu"
    assert isinstance(norm["last_seen"], datetime)
