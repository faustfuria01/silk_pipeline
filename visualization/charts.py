import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from collections import Counter
from typing import List


def plot_os_distribution(hosts: List[dict], output_path="charts/os_distribution.png"):
    """
    Plots the distribution of hosts by operating system.
    """
    os_list = [host["os"] for host in hosts]
    os_count = Counter(os_list)

    plt.figure(figsize=(8, 6))
    plt.bar(os_count.keys(), os_count.values())
    plt.title("Distribution of Hosts by Operating System")
    plt.xlabel("Operating System")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_host_age(hosts: List[dict], output_path="charts/host_age.png"):
    """
    Plots a graph comparing the number of old (more than 30 days old) and new hosts.
    """
    now = datetime.now()
    old_threshold = now - timedelta(days=30)

    old_hosts = [host for host in hosts if host["last_seen"] < old_threshold]
    new_hosts = [host for host in hosts if host["last_seen"] >= old_threshold]

    labels = ['Old Hosts (>30 days)', 'New Hosts']
    counts = [len(old_hosts), len(new_hosts)]

    plt.figure(figsize=(6, 6))
    plt.bar(labels, counts, color=['red', 'green'])
    plt.title("Old Hosts vs New Hosts")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
