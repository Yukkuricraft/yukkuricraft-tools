#!/bin/bash
source secrets/config
REPO_DIRS=($(echo $REPO_PATHS_SECRET | tr ':' "\n"))

for REPO_DIR in "${REPO_DIRS[@]}"
do
    chdir $REPO_DIR
    git pull
done
