#!/usr/bin/python

import psutil
import requests
import subprocess
from datetime import datetime
import secrets.discord_secrets as secrets

DEFAULT_THRESHOLD = 85.0
DEVICES = {
    # Dict[str, Tuple[str, float]] - Key is human readable name. Tuple vals are path and disk usage percent to alert on
    "OS Drive Root Partition": ("/", DEFAULT_THRESHOLD),
    "OS Drive Home Partition": ("/home", DEFAULT_THRESHOLD),
    "YC2.0 Data Disk": ("/var/lib/yukkuricraft", DEFAULT_THRESHOLD),
    "Primary Backup Disk": ("/media/backups-primary", DEFAULT_THRESHOLD),
    "Archives Backup Disk": ("/media/backups-archive", DEFAULT_THRESHOLD),
}

for dev_name, data in DEVICES.items():
    path, threshold_percentage = data
    percent_used = psutil.disk_usage(path)[3]
    if percent_used > threshold_percentage:
        payload = {
            "content": "Yo (%s), the `%s` is over %.2f%% disk space usage. You should clean it up. Currently at %.2f%%"
            % (secrets.REMI_USER_ID, dev_name, threshold_percentage, percent_used)
        }

        requests.post(
            secrets.DISCORD_WEBHOOK_URL,
            json=payload,
            headers={"content-type": "application/json"},
        )
