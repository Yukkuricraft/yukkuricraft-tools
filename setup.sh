#!/bin/bash

# NOTE: Make sure to run this from root of repo.

# First make sure we pull down our secrets
#git submodule update

# Setups up the not-really-vendors folder with PHPMailer

if [ -d not-really-vendors ]; then
    rm -rf not-really-vendors # If it exists, just delete and redownload shit incase something went wrong
fi

if [ -d PHPMailer-master ]; then
    rm -rf PHPMailer-master
fi

wget https://github.com/PHPMailer/PHPMailer/archive/master.zip
unzip master.zip
mkdir not-really-vendors
mv PHPMailer-master not-really-vendors/PHPMailer
rm master.zip

# Makes sure prev_known_ip exists.
PREV_KNOWN_IP_LOC=$(php -r "require_once('ip_check.php'); echo IP_Checker::PREV_IP_FILE_LOC;")
touch $PREV_KNOWN_IP_LOC

