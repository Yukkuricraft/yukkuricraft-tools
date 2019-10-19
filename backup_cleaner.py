#!/usr/bin/python

import os
import re
import sys
import time
from datetime import datetime
from itertools import chain

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
        # Special Notes:
        # - Given the "rough"/"guesstimating" nature of the time calculations/thresholds, this script becomes less effective the older the backups get. Particularly once you get into year-long ranges.
        "SIEVE_CONFIG": {
            '4h': 6 * 6, # 36: six days worth of standard 4 hour backups
            '1d': 7 * 3, # 21: three weeks worth of backups all minimum 24 hours apart
            '1w': 4 * 2, #  8: 2 months worth, all 1 week apart
            '6m': 4,     #  4: 2 years, all 6 months apart
        },
        "FOLDER_CONFIG": {
            # SEARCH_FOLDERS are folders that contain "folders to clean up". This should point at the "worlds" folder and the "plugins" folder, eg.
            # Both of these folders contain a list of folders which contain the actual backups we want to clean up.
            # Note: We only search with a depth of 1. That is to say, if you have a folder with folders you want cleaned that's two levels deep, we will not account for it.
            "SEARCH_FOLDERS": [
                "/media/backups/YukkuriCraft/PermaBackups/remi_backups/plugins",
                "/media/backups/YukkuriCraft/PermaBackups/remi_backups/worlds",
            ],
            # BLOCKED_SEARCH_FOLDERS are explicitly blacklisted "search folders". That is to say, any folder found inside a BLOCKED_SEARCH_FOLDERS folder will be blacklisted.
            "BLOCKED_SEARCH_FOLDERS": [
            ],
            # SINGLE_FOLDERS is basically a single folder which contains backups to clean up. This is for one-off backup locations or the like.
            "SINGLE_FOLDERS": [
                #"/media/backups/YukkuriCraft/PermaBackups/remi_backups/worlds/FF6",
            ],
            # BLOCKED_SINGLE_FOLDERS are an explicit list of blacklisted folders. This the single-folder version of BLOCKED_SEARCH_FOLDERS
            "BLOCKED_SINGLE_FOLDERS": [
            ],
        },
    },
]

MINIMUM_BACKUP_SIZE = 100 # bytes

def convertToEpoch(dt):
    return (dt - datetime(1970,1,1)).total_seconds()

def parseConf(config):
    acro_map = {
        #    min  hr   day, etc
        "h": 60 * 60,
        "d": 60 * 60 * 24,
        "w": 60 * 60 * 24 * 7,
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

def deleteInvalidSizeBackups(path):
    global MINIMUM_BACKUP_SIZE
    backups = os.listdir(path)

    for fname in backups:
        full_path = "%s/%s" % (path, fname)
        if os.path.getsize(full_path) < MINIMUM_BACKUP_SIZE:
            os.remove(full_path)

def genFileToEpochMap(path):
    global MINIMUM_BACKUP_SIZE
    backups = os.listdir(path)
    backups.sort()
    mapping = {}

    for fname in backups:
        full_path = "%s/%s" % (path, fname)
        r = re.compile(r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}")
        result = r.search(fname)

        timestamp = result.group()
        epoch_timestamp = convertToEpoch(datetime.strptime(timestamp, "%Y-%m-%d_%H-%M"))

        mapping[full_path] = epoch_timestamp
    return mapping


def returnBackupsToKeep(conf, file_to_epoch_map):
    now = int(time.time())

    file_epoch_list = [(path, epoch) for path, epoch in file_to_epoch_map.items()]
    file_epoch_list.sort(key=lambda tup: tup[1], reverse=True)
    total_backups = len(file_epoch_list)

    slots = {}

    index = 0

    conf_ordered = [(rule, count) for rule, count in conf.items()]
    conf_ordered.sort()

    for rule, count in conf_ordered:
        slots[rule] = []
        #print
        #print(slots)
        #print(rule, count)

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
                #print("Got all backups in %s's category's slots" % (rule))
                #for item in slots[rule]:
                #    print(repr(item))
                break

        if index > total_backups:
            break

    return slots

def getOldestTimestamp(slots):
    rule_strings = list(slots.keys());
    rule_strings.sort(reverse=True)

    min_timestamp = None
    for rule_string in rule_strings:
        tups = slots[rule_string]
        if len(tups) > 0:
            for tup in tups:
                timestamp = tup[1]
                if min_timestamp == None or timestamp < min_timestamp:
                    #print ("==",tup[0], timestamp)
                    min_timestamp = timestamp
            # Can do a break because we go from largest rule_string to smallest, meaning any subsequent loop must necessarily be a smaller rule_string, and therefore
            # the backups in the subsequent rule_string categories must be newer than the current category.
            break

    return min_timestamp

def findAllFilesToDelete(slots, file_to_epoch_map):
    oldest_timestamp_to_keep = getOldestTimestamp(slots)
    all_backups = file_to_epoch_map.keys()
    all_backups.sort(reverse=True)

    # Grab all tups in each rule_string category. But first filter out any rule_string categories that are empty.
    to_save_tmp = map(lambda tups: [tup[0] for tup in tups],
                      filter(lambda tups: len(tups) > 0,
                             slots.values()))
    to_save = set(chain.from_iterable(to_save_tmp))
    to_delete = []

    for backup in all_backups:
        timestamp = file_to_epoch_map[backup]
        if timestamp < oldest_timestamp_to_keep:
            #print "Breaking due to oldness - %s" % backup
            break
        if backup in to_save:
            #print "Save this one - %s" % backup
            continue
        #print "Deleting %s" % backup
        to_delete.append(backup)

    return to_delete

def consolidateFolderConf(folder_conf):
    SEARCH_FOLDERS = folder_conf["SEARCH_FOLDERS"]
    SINGLE_FOLDERS = folder_conf["SINGLE_FOLDERS"]

    BLOCKED_SEARCH_FOLDERS = folder_conf["BLOCKED_SEARCH_FOLDERS"]
    BLOCKED_SINGLE_FOLDERS = folder_conf["BLOCKED_SINGLE_FOLDERS"]

    all_folders = []
    blocked_folders = []

    for folder_root in SEARCH_FOLDERS:
        root = folder_root.rstrip("/")
        folder_names = os.listdir(root)
        all_folders.extend(map(lambda folder_name: "%s/%s" % (folder_root, folder_name), folder_names))

    for folder_root in BLOCKED_SEARCH_FOLDERS:
        root = folder_root.rstrip("/")
        folder_names = os.listdir(root)
        blocked_folders.extend(map(lambda folder_name: "%s/%s" % (folder_root, folder_name), folder_names))

    all_folders.extend(SINGLE_FOLDERS)
    blocked_folders.extend(BLOCKED_SINGLE_FOLDERS)

    all_folders = filter(lambda folder: folder not in blocked_folders, all_folders)

    return all_folders

def runConfig(sieve_conf, folder_conf):
    flattened_folder_conf = consolidateFolderConf(folder_conf)
    for folder_path in flattened_folder_conf:
        print
        print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        print "LOOKING AT %s" % folder_path
        deleteInvalidSizeBackups(folder_path)
        file_to_epoch_map = genFileToEpochMap(folder_path)
        #print(repr(file_to_epoch_map))

        slots = returnBackupsToKeep(sieve_conf, file_to_epoch_map)
        to_delete = findAllFilesToDelete(slots, file_to_epoch_map)

        for backup_to_delete in to_delete:
            print backup_to_delete
            os.remove(backup_to_delete)


def run():
    global CONFIGS
    for config in CONFIGS:
        sieve_conf = parseConf(config["SIEVE_CONFIG"])
        runConfig(sieve_conf, config["FOLDER_CONFIG"])

if __name__ == '__main__':
    run()
