import json
import time

import pandas as pd
from datasketch import HyperLogLog


def load_log_file(file_path):
    """
    Load the log file containing IP addresses in JSON format.
    Ignores incorrect or missing data lines.

    :param file_path: path to the log file.
    :return: list of IP addresses.
    """
    ip_addresses = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                data = json.loads(line.strip())
                ip = data.get("remote_addr")
                if ip:
                    ip_addresses.append(ip)
            except (json.JSONDecodeError, KeyError):
                continue
    return ip_addresses


def approximate_unique_count(ip_addresses):
    """
    :param ip_addresses: list of IP addresses.
    :return: approximate number of unique IP addresses.
    """
    hll = HyperLogLog()
    for ip in ip_addresses:
        hll.update(ip.encode('utf-8'))
    return len(hll)


if __name__ == "__main__":
    log_file_path = "lms-stage-access.log"
    ip_addresses = load_log_file(log_file_path)
    print("Number of IP addresses:", len(ip_addresses))

    # Count the number of unique elements using set
    start_time = time.time()
    exact_count = len(set(ip_addresses))
    exact_time = time.time() - start_time

    # Approximate count using HyperLogLog
    start_time = time.time()
    approx_count = approximate_unique_count(ip_addresses)
    approx_time = time.time() - start_time
    results = {
        "Method": ["Exact Count", "HyperLogLog"],
        "Unique Elements": [exact_count, approx_count],
        "Execution Time (sec)": [exact_time, approx_time]
    }
    df_results = pd.DataFrame(results)
    print("Results:")
    print(df_results)
