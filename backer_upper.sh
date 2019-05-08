#!/bin/bash

# This script will simply take the newest file in $BACKUP_DIR and move it to $PERMANENT_BACKUP_DIR

source secrets/backer_upper_secrets
NEWEST_FILE=$(ls -t $BACKUP_DIR | head -1)

cp $BACKUP_DIR/$NEWEST_FILE $PERMANENT_BACKUP_DIR

echo "[$(date --iso-8601=seconds)] Backed up $NEWEST_FILE to $PERMANENT_BACKUP_DIR"
