#!/usr/bin/python

import requests
import subprocess
from datetime import datetime
import secrets.discord_secrets as secrets

OUT_OF_DISK_STRING = "gzip: stdout: No space left on device"
BACKUP_LOG_PATH = "/var/log/crons/backup.log"

normal = subprocess.Popen(
    ["grep", "-o", OUT_OF_DISK_STRING, BACKUP_LOG_PATH],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
grep_stdout = normal.communicate()[0]

out_of_space = len(grep_stdout) > 0

if out_of_space:
    payload = {
        "content": "Hey Dipshit (%s), the backup disk is out of space."
        % (secrets.REMI_USER_ID),
    }

    requests.post(
        secrets.DISCORD_WEBHOOK_URL,
        json=payload,
        headers={"content-type": "application/json"},
    )
else:
    print "[%s] Good job, dumbass. You have diskspace for today." % (
        datetime.now().strftime("%Y-%m-%d")
    )
