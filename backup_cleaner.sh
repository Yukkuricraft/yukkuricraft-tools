#!/bin/bash

STRING="GapRealm-2019-07-17_12-01.tar.gz"

TIMESTRING=$(echo $STRING | sed 's/.*-\([0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}\)_\([0-9]\{2\}\)-\([0-9]\{2\}\).tar.gz/\1 \2:\3/g')
echo $TIMESTRING
TIMESTRING=$(date --date="$TIMESTRING" +"%s")

echo $TIMESTRING
