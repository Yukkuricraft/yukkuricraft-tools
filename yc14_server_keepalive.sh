#!/bin/bash

NAME=Yukkuricraft
SCREEN_NAME=yukkuricraft14
JAR_FILE="paper-172-async.jar"
JAR_PATH="/home/minecraft/YC/YukkuriCraft"
RAM=24G

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
        -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 \
        -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled \
        -XX:-UseBiasedLocking -XX:+ExplicitGCInvokesConcurrent \
        -Xss8m \
        -jar "$JAR_PATH/$JAR_FILE"
