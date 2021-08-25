#!/bin/bash

MIN_COOLDOWN_TO_RESTART=120 # seconds.
MIKO_DIR="/home/minecraft/YC/Miko2/"
MIKO_START_SCRIPT="startMiko.sh"
NOW=$(date +"%s")

log () {
    echo "[$(date +"%Y-%m-%d_%H-%M")] $@"
}

IS_RUNNING=$(ps aux | grep Miko2 | grep SCREEN)
if [ -n "$IS_RUNNING" ]; then
    log "Miko is running. Aborting."
    exit 0
fi

STATUS_CHECK_FILE="/home/minecraft/YC/yukkuricraft-tools/MIKO_KEEPALIVE_STATUS"
if [ ! -f "$STATUS_CHECK_FILE" ]; then
    touch $STATUS_CHECK_FILE
fi

# Miko is not running
LAST_CHECKED=$(cat $STATUS_CHECK_FILE)
if [ -z "$LAST_CHECKED" ]; then
    # First time we're confirming Miko is down. Log timestamp.
    log "Detected Miko being down for the first time. Logging. Will restart if still down in $MIN_COOLDOWN_TO_RESTART seconds."
    log $NOW > $STATUS_CHECK_FILE
    exit 0
fi

if [ $NOW -ge $(($LAST_CHECKED + $MIN_COOLDOWN_TO_RESTART)) ]; then
    log "Cooldown elapsed. Restarting Miko2..."
    (cd $MIKO_DIR && $MIKO_DIR/$MIKO_START_SCRIPT)

    if [ $? -ne 0 ]; then
        log "FAILED TO START MIKO?"
        exit 1
    fi

    log "Clearing out $STATUS_CHECK_FILE"
    log "" > $STATUS_CHECK_FILE
else
    log "Still waiting on cooldown to restart Miko2. Waiting for $(($MIN_COOLDOWN_TO_RESTART - $NOW + $LAST_CHECKED)) more seconds."
fi
