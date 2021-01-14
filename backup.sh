#!/bin/bash

containsElement () {
    local e match="$1"
    shift
    for e; do [[ "$e" == "$match" ]] && return 0; done
    return 1
}

SCRIPT_PATH=$(dirname $(readlink -f $0))
source $SCRIPT_PATH/secrets/backer_upper_secrets
WORLDS_BACKUP_DIR=$PERMANENT_BACKUP_DIR/worlds
PLUGINS_BACKUP_DIR=$PERMANENT_BACKUP_DIR/plugins

# This assumes the screen name created by /etc/init.d/minecraft is "yukkuricraft" as defined in that file.
SCREENNAME="yukkuricraft"

SCREEN_RUNNING=$(screen -S $SCREENNAME -Q select . > /dev/null ; echo $?)

if [ $SCREEN_RUNNING != "0" ]; then
    echo "Screen by name $SCREENNAME does not seem to be running. Is Minecraft up?"
    exit 1
fi

ENTERKEY='\015'
# Sends the 'save-off' command to the screen. $(echo) at end to emulate user hitting "enter" in the Screen.
screen -S $SCREENNAME -X stuff 'save-off'$(echo -ne $ENTERKEY)

BASE_SERVER_PATH='/home/minecraft/YC/YukkuriCraft'

WORLDS_TO_BACKUP=(
    "CreativeFlat"
    "FF6"
    "GapRealm"
    "Gensokyo"
    "Heaven"
    "Makai"
    "NeoGensokyo"
    "NewHaku"
    "Survival4"
    "Survival4_nether"
    "Survival4_the_end"
    "PB_Gensokyo"
    "Senkai"
    "Statues"
)

for WORLD in "${WORLDS_TO_BACKUP[@]}"; do
    FULL_WORLD_PATH="$BASE_SERVER_PATH/$WORLD/"
    FULL_BACKUP_PATH="$WORLDS_BACKUP_DIR/$WORLD"

    if [ ! -d "$FULL_BACKUP_PATH" ]; then
        mkdir -p "$FULL_BACKUP_PATH"
    fi

    NOW=$(date +"%Y-%m-%d_%H-%M")
    BACKUP_NAME="$WORLD-$NOW.tar.gz"
    TRANSFORM_EXP="s|^|$WORLD/|"

    echo "[$NOW] Tarring up $FULL_WORLD_PATH..."
    tar -zcf "$FULL_BACKUP_PATH/$BACKUP_NAME" --transform "$TRANSFORM_EXP" -C "$FULL_WORLD_PATH" .
    echo "[$(date +"%Y-%m-%d_%H-%M")] Archive saved to $FULL_BACKUP_PATH/$BACKUP_NAME."
done

PLUGIN_PATH="$BASE_SERVER_PATH/plugins"

PLUGINS_TO_IGNORE=(
   "dynmap"
)

PLUGIN_DIR_CONTENT=$PLUGIN_PATH/*
for FULL_PLUGIN_PATH in $PLUGIN_DIR_CONTENT; do
    [ -d "$FULL_PLUGIN_PATH" ] || continue

    PLUGIN_NAME=$(basename $FULL_PLUGIN_PATH)

    containsElement $PLUGIN_NAME $PLUGINS_TO_IGNORE
    [[ $? == 1 ]] || continue

    FULL_BACKUP_PATH="$PLUGINS_BACKUP_DIR/$PLUGIN_NAME"

    if [ ! -d "$FULL_BACKUP_PATH" ]; then
        mkdir -p "$FULL_BACKUP_PATH"
    fi

    NOW=$(date +"%Y-%m-%d_%H-%M")
    BACKUP_NAME="$PLUGIN_NAME-$NOW.tar.gz"
    TRANSFORM_EXP="s|^|$PLUGIN_NAME/|"

    echo "[$NOW] Tarring up $FULL_PLUGIN_PATH..."
    tar -zcf "$FULL_BACKUP_PATH/$BACKUP_NAME" --transform "$TRANSFORM_EXP" -C "$FULL_PLUGIN_PATH" .
    echo "[$(date +"%Y-%m-%d_%H-%M")] Archive saved to $FULL_BACKUP_PATH/$BACKUP_NAME."
done


# And 'save-on' once backup is done.
screen -S $SCREENNAME -X stuff 'save-on'$(echo -ne $ENTERKEY)
