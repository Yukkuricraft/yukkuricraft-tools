#!/bin/bash

containsElement () {
    local e match="$1"
    shift
    for e; do [[ "$e" == "$match" ]] && return 0; done
    return 1
}

log () {
    echo "[$(date +"%Y-%m-%d_%H-%M")] $@"
}

SCRIPT_PATH=$(dirname $(readlink -f $0))

# Auth with gcloud first.
SA_JSON_FILE=$SCRIPT_PATH/secrets/yc-gsutil-sa.json
gcloud auth activate-service-account --key-file $SA_JSON_FILE

source $SCRIPT_PATH/secrets/backer_upper_secrets
WORLDS_BACKUP_DIR=$PERMANENT_BACKUP_DIR/worlds
PLUGINS_BACKUP_DIR=$PERMANENT_BACKUP_DIR/plugins
GCS_UPLOAD_URI=$GCS_BUCKET_URI/$(date +"%Y-%m-%d")

for WORLD in "${WORLDS_TO_BACKUP[@]}"; do
    BACKUP_PATH="$WORLDS_BACKUP_DIR/$WORLD"
    NEWEST_FILE=$(ls -t $BACKUP_PATH | head -1)

    log "Uploading $NEWEST_FILE to GCS..."
    gsutil cp $BACKUP_PATH/$NEWEST_FILE $GCS_UPLOAD_URI/worlds/
    log "Archive uploaded to $GCS_UPLOAD_URI/worlds/$NEWEST_FILE."
done

PLUGIN_DIR_CONTENT=$PLUGINS_BACKUP_DIR/*
for PLUGIN_PATH in $PLUGIN_DIR_CONTENT; do
    [ -d "$PLUGIN_PATH" ] || continue

    PLUGIN_NAME=$(basename $PLUGIN_PATH)
    containsElement $PLUGIN_NAME $PLUGINS_TO_IGNORE
    [[ $? == 1 ]] || continue

    BACKUP_PATH="$PLUGINS_BACKUP_DIR/$PLUGIN_NAME"
    NEWEST_FILE=$(ls -t $BACKUP_PATH | head -1)

    log "Uploading $NEWEST_FILE to GCS..."
    gsutil cp $BACKUP_PATH/$NEWEST_FILE $GCS_UPLOAD_URI/plugins/
    log "Archive uploaded to $GCS_UPLOAD_URI/plugins/$NEWEST_FILE."
done
