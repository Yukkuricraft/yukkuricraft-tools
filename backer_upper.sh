#!/bin/bash

# This script will simply take the newest file in $BACKUP_DIR and move it to $PERMANENT_BACKUP_DIR


# This assumes it's running on Ubuntu really.
# It's nigh impossible to have a 100% platform-independent way of getting script path so I just used one specific to our ubuntu install.
SCRIPT_PATH=$(dirname $(readlink -f $0))

source $SCRIPT_PATH/secrets/backer_upper_secrets
NEWEST_FILE=$(ls -t $BACKUP_DIR | head -1)

cp $BACKUP_DIR/$NEWEST_FILE $PERMANENT_BACKUP_DIR

echo "[$(date --iso-8601=seconds)] Backed up $NEWEST_FILE to $PERMANENT_BACKUP_DIR"
