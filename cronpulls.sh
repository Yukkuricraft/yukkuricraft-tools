#!/bin/bash
source secrets/config
REPO_DIRS=($(echo $REPO_PATHS_SECRET | tr ':' "\n"))

for REPO_DIR in "${REPO_DIRS[@]}"
do
    (cd $REPO_DIR && git pull) # Can't use chdir in bash script unless in function... or just do this.
done
