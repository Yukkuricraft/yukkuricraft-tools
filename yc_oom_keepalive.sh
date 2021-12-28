#!/bin/bash

# MUST BE RUN AS ROOT

YC_PROCESS_ID=$(ps aux | grep "yukkuricraft18" | grep "SCREEN" | grep -o "[0-9]\+" | head -1)

if [ "$YC_PROCESS_ID" == "" ]; then
    echo "Yukkuricraft not running! Or at least couldn't find its screen!"
    exit 1
fi

OOM_ADJ_PATH="/proc/$YC_PROCESS_ID/oom_adj"

echo "-17" > $OOM_ADJ_PATH
