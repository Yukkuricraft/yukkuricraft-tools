#!/bin/bash

# Setups up the not-really-vendors folder with PHPMailer
wget https://github.com/PHPMailer/PHPMailer/archive/master.zip
unzip master.zip -d PHPMailer
rm master.zip

# Makes sure prev_known_ip exists.
PREV_KNOWN_IP_LOC=$(php -r "require_once('ip_check.php'); echo IP_Checker::PREV_IP_FILE_LOC;")
touch $PREV_KNOWN_IP_LOC
