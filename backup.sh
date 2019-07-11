#!/bin/bash

SCRIPT_PATH=$(dirname $(readlink -f $0))
source $SCRIPT_PATH/secrets/backer_upper_secrets
WORLDS_BACKUP_DIR=$PERMANENT_BACKUP_DIR/remi_backups/worlds

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

BASE_WORLDS_PATH='/home/minecraft/YC/YukkuriCraft'
WORLDS_TO_BACKUP=(
        "CreativeFlat"
        "FF6"
        "GapRealm"
        "Gensokyo"
        "Heaven"
        "Makai"
        "NeoGensokyo"
        "NewHaku"
        "NewYoukaiMountain"
        "NovaSurvival"
        "NovaSurvival_nether"
        "NovaSurvival_the_end"
        "PB_Gensokyo"
        "Sakuya's World"
        "Senkai"
        "Statues"
)

for WORLD in "${WORLDS_TO_BACKUP[@]}"; do
        FULL_WORLD_PATH="$BASE_WORLDS_PATH/$WORLD/"
        FULL_BACKUP_PATH="$WORLDS_BACKUP_DIR/$WORLD"

        if [ ! -d "$FULL_BACKUP_PATH" ]; then
                mkdir -p "$FULL_BACKUP_PATH"
        fi

        BACKUP_NAME="$WORLD-$(date +"%Y-%m-%d_%H-%M").tar.gz"
        TRANSFORM_EXP="s|^|$WORLD/|"
        tar -zcf "$FULL_BACKUP_PATH/$BACKUP_NAME" --transform "$TRANSFORM_EXP" -C "$FULL_WORLD_PATH" .
done


# And 'save-on' once backup is done.
screen -S $SCREENNAME -X stuff 'save-on'$(echo -ne $ENTERKEY)
