#!/bin/bash

# This assumes it's running on Ubuntu really.
# It's nigh impossible to have a 100% platform-independent way of getting script path so I just used one specific to our ubuntu install.
SCRIPT_PATH=$(dirname $(readlink -f $0))

source $SCRIPT_PATH/secrets/config
REPO_DIRS=($(echo $REPO_PATHS_SECRET | tr ':' "\n"))

for REPO_DIR in "${REPO_DIRS[@]}"
do
    echo "Executing 'git pull' in $REPO_DIR"
    (cd $REPO_DIR && git pull) # Can't use chdir in bash script unless in function... or just do this.
done
