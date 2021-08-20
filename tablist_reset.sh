#!/bin/bash

# This assumes the screen name created by /etc/init.d/minecraft is "yukkuricraft" as defined in that file.
SCREENNAME="yukkuricraft"

SCREEN_RUNNING=$(screen -S $SCREENNAME -Q select . > /dev/null ; echo $?)

if [ $SCREEN_RUNNING != "0" ]; then
    echo "Screen by name $SCREENNAME does not seem to be running. Is Minecraft up?"
    exit 1
fi

ENTERKEY='\015'
# Sends the 'save-off' command to the screen. $(echo) at end to emulate user hitting "enter" in the Screen.
screen -S $SCREENNAME -X stuff 'plugman reload tablist'$(echo -ne $ENTERKEY)
