#!/bin/bash

NAME=Yukkuricraft
SCREEN_NAME=yukkuricraft17
JAR_FILE="paper-1.17-75.jar"
JAR_PATH="/home/minecraft/YC/YukkuriCraft"
RAM=16G

###################

log () {
    echo $(date +"[%Y-%m-%d %H:%M]") $@
}

PROCESS_ID=$(ps aux | grep "$SCREEN_NAME" | grep "SCREEN" | grep -o "[0-9]\+" | head -1)

if [ "$PROCESS_ID" != "" ]; then
    log "$NAME's screen was running - Assuming server is alive!"
    exit 1
fi

log "Could not find $NAME's screen running! Restarting..."

cd $JAR_PATH

screen -dmS $SCREEN_NAME \
        java -Xms${RAM} -Xmx${RAM} \
        -Duser.dir=${JAR_PATH} \
        -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 \
        -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC \
        -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 \
        -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 \
        -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 \
        -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 \
        -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 \
        -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true \
        -jar "$JAR_PATH/$JAR_FILE" nogui
