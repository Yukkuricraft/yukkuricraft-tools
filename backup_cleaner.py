import os
import re
import sys
import time
from datetime import datetime

# This is our backup cleaner script.
# This script makes no strong guarantees other than that:
# - Each backup in its own category is a minimum of `RULE_STRING` time apart from each other backup in its category
# - That the newest backup in each category is a minimum age of the sum of all smaller categories combined
#   (The "sum of a category" is defined as the RULE_STRING multiplied by the number of backups in that category to take, eg 6h * 4 = 24h is the sum)

# Can have multiple configs for separate folders.
CONFIGS = [
    {
        # key is the "rule", or RULE_STRING, which is minimum delta of seconds between each backup
        # val is count of how many of backups in that delta you want
        #
        # Each rule "appends" to each other.
        # Eg, if the rules are "12h" for 2 counts, "3d" for 5 counts, and "1w" for 4 counts what you would get is
        # 2 backups that are at least 12 hours apart,
        # 5 backups that are at least 72 hours apart that are a minimum of 24 hours old (ie, 2 * 12hr)
        # 4 backups that are at least 168 hours apart that are a minimum of 384 hours old (ie, 24 + (5 * 72)
        # Note that because of the above logic only having a _minimum_ age, this means your oldest backup can be much older than just the pure sum of all categories.
        #
        # Special syntax:
        # - Adding '\+\-[0-9]{2}%' to the end of a rule string means the logic will allow for a "plus minus <num> percentage variation" of the delta length.
        #   ie, if you have a 1y+-10%, then that means you want backups that are ideally minimum 1y apart, but if you want to retain old backups without deleting them because
        #   the file in question missed the 1y threshold by say just a month, perhaps you want to actually retain the file. Basically, this is for making your spacing length more lenient
        #   Ask Remi if you need clarification. This is a stupid config.
        #
        # Special Notes:
        # - Similar to above, the default threshold value is 1%. That is to say, if you wanted each backup to be at least 1000 seconds apart, by default
        #   this script will allow for backups to actually be a minimum of _990_ seconds (1000 * 0.99) apart. This is to account for the fact that even if backups are made exactly 1000 seconds apart,
        #   given real world scenarios these backups might be some small # of seconds off.
        # - Given the "rough"/"guesstimating" nature of the time calculations/thresholds, this script becomes less effective the older the backups get. Particularly once you get into year-long ranges.
        "SIEVE_CONFIG": {
            '4h': 6,# * 7, # one week worth of standard 6 hour backups
            '1d': 7,# * 4, # one month worth of backups all minimum 24 hours apart
            '1w': 4,# * 4, # 4 months worth, all 1 week apart
            '6m+-10%': 4,# 2 years, all 6 months apart
        },
        "FOLDER_ROOTS": [
            "/media/backups/YukkuriCraft/PermaBackups/remi_backups/plugins",
            "/media/backups/YukkuriCraft/PermaBackups/remi_backups/worlds",
        ],
    },
]

def parseConf(config):
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
        epoch_timestamp = int(datetime.strptime(timestamp, "%Y-%m-%d_%H-%M").timestamp())

        mapping[f"{path}/{fname}"] = epoch_timestamp
    return mapping


def returnBackupsToKeep(conf, file_to_epoch_map):
    now = int(time.time())

    file_epoch_list = [(path, epoch) for path, epoch in file_to_epoch_map.items()]
    file_epoch_list.sort(key=lambda tup: tup[1], reverse=True)
    total_backups = len(file_epoch_list)

    slots = {}

    index = 0
    for rule, count in conf.items():
        slots[rule] = []
        print(slots)
        print(rule, count)

        saved = 0

        for tup in file_epoch_list[index:]:
            #print(tup)
            path, timestamp = tup
            age = now - timestamp
            prev_backup_timestamp = slots[rule][-1][1] if len(slots[rule]) >= 1 else -1
            delta_from_prev_backup = prev_backup_timestamp - timestamp
            #print("Prev backup from: ", prev_backup_timestamp, "# Secs since prev:", delta_from_prev_backup)
            if delta_from_prev_backup >= rule or prev_backup_timestamp == -1:
                #print("This one good for backup:", path, age)
                slots[rule].append(tup)

            index += 1
            if len(slots[rule]) >= count:
                print("Got all backups in this category's slots")
                for item in slots[rule][:5]:
                    print(repr(item))
                break

        if index > total_backups:
            break

    return slots

def getOldestTimestamp(slots):
    keys = list(slots.keys());
    keys.sort(reverse=True)

    min_timestamp = None
    for key in keys:
        tups = slots[key]
        if len(tups) > 0:
            for tup in tups:
                timestamp = tup[1]
                if min_timestamp == None or timestamp < min_timestamp:
                    min_timestamp = timestamp
            break

    return min_timestamp

def findAllFilesToDelete(slots):
    oldest_timestamp_to_keep = getOldestTimestamp(slots)


def runConfig(sieve_conf, folder_conf):
    print(repr(sieve_conf))
    for root in folder_conf:
        root = root.rstrip("/")
        folders = os.listdir(root)

        for folder in folders:
            path = f"{root}/{folder}"
            file_to_epoch_map = genFileToEpochMap(path)
            #print(repr(file_to_epoch_map))

            slots = returnBackupsToKeep(sieve_conf, file_to_epoch_map)
            to_delete = findAllFilesToDelete(slots)

            break
        break


def run():
    global CONFIGS
    for config in CONFIGS:
        sieve_conf = parseConf(config["SIEVE_CONFIG"])
        runConfig(sieve_conf, config["FOLDER_ROOTS"])

if __name__ == '__main__':
    run()
