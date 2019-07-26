import os
import re
import sys
from datetime import datetime

config = {
    'config1_this_fieldname_doesnt_matter': {
        'cadence': {
            '6h': 4 * 7, # one week
            '1w': 4 * 4, # 4 months
            '6m': 4, # 2 years
        },
        'folders': {
            'worlds': [
                'CreativeFlat'
            ],
        }
    }
}

def parseConfField(config_field):
    num = `config_field`[0]

TIMESTAMP_FMT = "%Y-%m-%d_%H-%M"

BASE_BACKUP_PATH = "/media/backups/YukkuriCraft/PermaBackups/remi_backups/"
BACKUP_PATH = BASE_BACKUP_PATH + "worlds/CreativeFlat" # idk just dev'ing for now
#backup_files_list = os.listdir(BACKUP_PATH)

backup_files_list = [
    "CreativeFlat-2019-08-11_16-14.tar.gz",
    "CreativeFlat-2019-08-01_16-14.tar.gz",
    "CreativeFlat-2019-07-25_16-14.tar.gz",
    "CreativeFlat-2019-07-25_10-14.tar.gz",
    "CreativeFlat-2019-07-25_10-00.tar.gz",
    "CreativeFlat-2019-07-20_16-14.tar.gz",
    "CreativeFlat-2019-06-11_20-14.tar.gz",
]
r_c = re.compile(r"(\d{4}-\d{2}-\d{2}_\d{2}-\d{2})")
for path in backup_files_list:
    result = r_c.search(path)

    timestamp = result.group()
    utc_timestamp = datetime.strptime(timestamp, TIMESTAMP_FMT);
    epoch_timestamp = int((utc_timestamp - datetime(1970,1,1)).total_seconds())

    print epoch_timestamp
