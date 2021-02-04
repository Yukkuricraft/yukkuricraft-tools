#!/usr/bin/python

import psutil
import requests
import subprocess
from datetime import datetime
import secrets.discord_secrets as secrets

DEVICES = {
    "Main Disk": ("/", 80.0), # Dict[str, Tuple[str, float]] - Key is human readable name. Tuple vals are path and disk usage percent to alert on
    #"Raid Backup Disk": ("/media/raidbackups", 85.0),
    "Primary Backup Disk": ("/media/backups-primary", 90.0),
    "Failover Backup Disk": ("/media/backups-failover", 98.0),
}

for dev_name, data in DEVICES.items():
    path, threshold_percentage = data
    percent_used = psutil.disk_usage(path)[3]
    if percent_used > threshold_percentage:
        payload = {
            "content": "Yo (%s), the `%s` is over %.2f%% disk space usage. You should clean it up."
            % (secrets.REMI_USER_ID, dev_name, threshold_percentage)
        }

        requests.post(
            secrets.DISCORD_WEBHOOK_URL,
            json=payload,
            headers={"content-type": "application/json"},
        )
