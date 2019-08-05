import os
import re
import sys
from datetime import datetime

CONFIGS = [
    {
        # key is the "rule", which is delta of seconds between each backup
        # val is count of how many of backups in that delta you want
        #
        # Each rule "appends" to each other.
        # Eg, if the rules are "12h" for 2 counts, "3d" for 5 counts, and "1w" for 4 counts what you would get is
        # 2 backups that are at least 12 hours apart,
        # 5 backups that are at least 72 hours apart that are a minimum of 24 hours old (ie, 2 * 12hr)
        # 4 backups that are at least 168 hours apart that are a minimum of 384 hours old (ie, 24 + (5 * 72)
        "SIEVE_CONFIG": {
            '6h': 4 * 7, # one week worth of standard 6 hour backups
            '1w': 4 * 4, # 4 months
            '6m': 4,     # 2 years
        },
        "FOLDER_ROOTS": [
            "/media/backups/YukkuriCraft/PermaBackups/remi_backups/plugins",
            "/media/backups/YukkuriCraft/PermaBackups/remi_backups/worlds",
        ],
    },
]

def parseConf(config):
    # to num of seconds - hour is smallest unit
    acro_map = {
        #    min  hr   day, etc
        "h": 60 * 60,
        "d": 60 * 60 * 24,
        "w": 60 * 69 * 24 * 7,
        "m": 60 * 60 * 24 * 7 * 4,
        "y": 60 * 60 * 24 * 365,
    }

    rules = {}
    for rule_str, count in config.items():
        delta_val = 0
        for acro, sec in acro_map.items():
            r = re.compile('(\d+)%s' % acro)
            matches = r.search(rule_str)
            if matches != None:
                delta_val += sec * int(matches.group(1))
        print(rule_str, delta_val)
        rules[delta_val] = count

    return rules

def genFileToEpochMap(path):
    backups = os.listdir(path)
    mapping = {}

    for fname in backups:
        r = re.compile(r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}")
        result = r.search(fname)

        timestamp = result.group()
        utc_timestamp = datetime.strptime(timestamp, "%Y-%m-%d_%H-%M");
        epoch_timestamp = int((utc_timestamp - datetime(1970,1,1)).total_seconds())

        mapping[f"{path}/{fname}"] = epoch_timestamp
    return mapping

def runConfig(sieve_conf, folder_conf):
    print(repr(sieve_conf))
    for root in folder_conf:
        root = root.rstrip("/")
        folders = os.listdir(root)

        for folder in folders:
            path = f"{root}/{folder}"
            file_to_epoch_map = genFileToEpochMap(path)

            print(repr(file_to_epoch_map))

            # TODO: process sieve rules on the map


def run():
    global CONFIGS
    for config in CONFIGS:
        sieve_conf = parseConf(config["SIEVE_CONFIG"])
        runConfig(sieve_conf, config["FOLDER_ROOTS"])

if __name__ == '__main__':
    run()


