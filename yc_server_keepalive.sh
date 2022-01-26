#!/bin/bash

NAME=Yukkuricraft
SCREEN_NAME=yukkuricraft18
JAR_FILE="paper-1.18.1-176.jar"
JAR_PATH="/home/minecraft/YC/YukkuriCraft"
JAVA_PATH="/home/minecraft/.sdkman/candidates/java/current/bin/java"
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
        $JAVA_PATH -Xms${RAM} -Xmx${RAM} \
        -Duser.dir=${JAR_PATH} \
        -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 \
        -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled \
        -XX:-UseBiasedLocking -XX:+ExplicitGCInvokesConcurrent \
        -Xss8m \
        -jar "$JAR_PATH/$JAR_FILE" nogui
