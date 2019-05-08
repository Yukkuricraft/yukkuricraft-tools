#!/bin/bash

# This script will simply take the newest file in $BACKUP_DIR and move it to $PERMANENT_BACKUP_DIR
# $BACKUP_DIR should be the path that AutoSaveWorld is configured to save to. In our case, probably just backups/YukkuriCraft/

# This assumes it's running on Ubuntu really.
# It's nigh impossible to have a 100% platform-independent way of getting script path so I just used one specific to our ubuntu install.
SCRIPT_PATH=$(dirname $(readlink -f $0))


source $SCRIPT_PATH/secrets/backer_upper_secrets

# Permastore newest plugins backup
PLUGINS_BACKUP_DIR=$BACKUP_DIR/backups/plugins
NEWEST_PLUGIN_BACKUP=$(ls -t $PLUGINS_BACKUP_DIR | head -1)
PERMANENT_PLUGINS_BACKUP_DIR=$PERMANENT_BACKUP_DIR/plugins

mkdir -p $PERMANENT_PLUGINS_BACKUP_DIR
cp $PLUGINS_BACKUP_DIR/$NEWEST_PLUGIN_BACKUP $PERMANENT_PLUGINS_BACKUP_DIR

echo "[$(date --iso-8601=seconds)] Backed up $NEWEST_PLUGIN_BACKUP to $PERMANENT_PLUGINS_BACKUP_DIR"

# Iterate through various worlds we save and save newest copy of each.

WORLDS_BACKUP_DIR=$BACKUP_DIR/backups/worlds/*

for path in $WORLDS_BACKUP_DIR; do
    # Quotes cuz that sakuya world has quotes in the folder name ._.
    [ -d "${path}" ] || continue

    WORLD_NAME=$(basename "${path}")
    NEWEST_WORLD_BACKUP=$(ls -t "${path}" | head -1)
    PERMANENT_WORLDS_BACKUP_DIR=$PERMANENT_BACKUP_DIR/worlds/$WORLD_NAME

    mkdir -p $PERMANENT_WORLDS_BACKUP_DIR
    cp "${path}/${NEWEST_WORLD_BACKUP}" $PERMANENT_WORLDS_BACKUP_DIR
    echo "[$(date --iso-8601=seconds)] Backed up $NEWEST_WORLD_BACKUP of $WORLD_NAME to $PERMANENT_WORLDS_BACKUP_DIR"
done
