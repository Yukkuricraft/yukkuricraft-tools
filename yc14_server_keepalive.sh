#!/bin/bash

# MUST BE RUN AS ROOT

log () {
    echo $(date +"[%Y-%m-%d %H:%M]") $@
}

YC_PROCESS_ID=$(ps aux | grep "yukkuricraft14" | grep "SCREEN" | grep -o "[0-9]\+" | head -1)
START_SCRIPT="/home/minecraft/YC/YukkuriCraft/start.sh"

if [ "$YC_PROCESS_ID" != "" ]; then
    log "YC screen was running - Assuming server is alive!"
    exit 1
fi

log "Could not find YC screen running! Restarting..."
$START_SCRIPT
