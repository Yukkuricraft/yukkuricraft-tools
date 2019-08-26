#!/bin/bash

# MUST BE RUN AS ROOT
# Cannot _lower_ oom scores without root access.

YC_PROCESS_ID=$(ps aux | grep "yukkuricraft14" | grep "SCREEN" | grep -o "[0-9]\+" | head -1)

if [ "$YC_PROCESS_ID" == "" ]; then
    echo "Yukkuricraft not running! Or at least couldn't find its screen!"
    exit 1
fi

OOM_SCORE_ADJ_PATH="/proc/$YC_PROCESS_ID/oom_score_adj"

echo "-1000" > $OOM_SCORE_ADJ_PATH
