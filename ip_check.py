#!/usr/bin/python3

import os
import sys
import re
import datetime
import getpass
import smtplib
import requests
import argparse
import logging
import secrets.ip_check_secrets as secrets
import traceback

from typing import Dict, Optional
from email.message import EmailMessage


class IP_Checker:
    IP_CHECK_URL = "checkip.dyndns.org"
    # IP_CHECK_URL = "orderofaxis.org"
    PREV_IP_FILE_LOC = f"/home/{getpass.getuser()}/prev_known_ip"

    LOG_LOC = "/var/log/minecraft/ip_checker_logs"
    LOG_MSG_FMT = "[%(levelname)s][%(asctime)s] %(message)s"
    LOG_TIMESTAMP_FMT = "%Y-%m-%dT%H:%M:%S%z"

    SENT_FROM_NAME = "Yukkuri Notifications"
    SUBJECT_FMT = "[Yukkuricraft] IP Change Detected on {}"
    BODY_FMT = "Hi nignogs.\n\nThis is an automagically generated email.\n\nPrev Server IP: {}\nNew Server IP: {}\n\nHave fun playing, nerds.\n~ RemiBot"
    EMAIL_RECIPIENT_FMT = "{} <{}>"

    def __init__(self, args: argparse.Namespace):
        self.prodrun = args.prodrun
        self.verbose = args.verbose

        log_level = logging.DEBUG if self.verbose else logging.INFO

        dirname = os.path.dirname(self.LOG_LOC)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        logging.basicConfig(
            filename=self.LOG_LOC,
            format=self.LOG_MSG_FMT,
            datefmt=self.LOG_TIMESTAMP_FMT,
            level=log_level,
        )
        self.logger = logging.getLogger(__name__)

    def __log(self, msg: str, level: Optional[int] = None):
        if level == logging.DEBUG:
            self.logger.debug(msg)
        elif level == None or level == logging.INFO:
            self.logger.info(msg)
        elif level == logging.WARNING:
            self.logger.warning(msg)
        elif level == logging.ERROR:
            self.logger.error(msg)
        print(f"[LOG][{datetime.datetime.now().isoformat()}] {msg}")

    IP_REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    IP_EXTRACT_REGEX = f"Current IP Address: (?P<curr_ip>{IP_REGEX})"

    def __getCurrIP(self) -> str:
        r = requests.get(f"http://{self.IP_CHECK_URL}")
        ip_re = re.compile(self.IP_EXTRACT_REGEX)
        results = ip_re.search(r.text)
        if results == None:
            raise InvalidResponseException(
                f"Got an invalid response from {self.IP_CHECK_URL}"
            )
        else:
            return results.group("curr_ip")

    def __getPrevIP(self) -> str:
        """
        If PREV_IP_FILE_LOC contains a string that does not match a plain ipv4 address, will return an empty string.
        In other words, we validate the contents to be a real IP.
        """
        if not os.path.exists(self.PREV_IP_FILE_LOC):
            return ""

        with open(self.PREV_IP_FILE_LOC, "r") as f:
            content = f.read()
            ip_re = re.compile(self.IP_REGEX)
            results = ip_re.search(content)

            if results == None:
                return ""
            else:
                return results.group()

    def __getNotificationRecipients(self) -> Dict[str, str]:
        if self.prodrun:
            return secrets.EMAILS_TO_SEND_TO
        else:
            return secrets.EMAILS_TO_SEND_TO_TEST

    def __generateRecipientString(self) -> str:
        recipient_string = ""

        recipients = self.__getNotificationRecipients()
        for index, name in enumerate(recipients.keys()):
            email = recipients[name]
            recipient_string += self.EMAIL_RECIPIENT_FMT.format(name, email)

            if index < len(recipients) - 1:
                recipient_string += ", "

        return recipient_string

    def __notifyAboutNewIP(self, new_ip: str, old_ip: str):
        recipients_string = self.__generateRecipientString()

        email_payload = EmailMessage()
        email_payload.set_content(self.BODY_FMT.format(old_ip, new_ip))
        email_payload["Subject"] = self.SUBJECT_FMT.format(
            datetime.datetime.now().isoformat()
        )
        email_payload["From"] = f"{self.SENT_FROM_NAME} <{secrets.REPLY_TO_EMAIL}>"
        email_payload["To"] = recipients_string

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(secrets.THROWAWAY_GMAIL_EMAIL, secrets.THROWAWAY_GMAIL_PASS)
            server.send_message(email_payload)
            server.quit()

            self.__log(
                f"IP Change detected and notified. Old IP: {old_ip}, New IP: {new_ip}"
            )
        except:
            traceback.print_exc()
            raise EmailFailedException(
                f"Failed to send email about new IP change. Prod run: {self.prodrun}"
            )

    def __writeNewIP(self, new_ip: str):
        with open(self.PREV_IP_FILE_LOC, "w") as f:
            f.write(new_ip)

    def run(self):
        try:
            new_ip = self.__getCurrIP()
            old_ip = self.__getPrevIP()
            if new_ip != old_ip:
                self.__notifyAboutNewIP(new_ip, old_ip)
                self.__writeNewIP(new_ip)
            else:
                self.__log("No IP change detected.")
        except InvalidResponseException as e:
            self.__log(e)
            sys.exit(1)
        except EmailFailedException as e:
            self.__log(e)
            sys.exit(1)
        except Exception as e:
            self.__log(f"Uncaught Exception: {e}")
            sys.exit(1)


class InvalidResponseException(Exception):
    pass


class EmailFailedException(Exception):
    pass


parser = argparse.ArgumentParser()
parser.add_argument(
    "-p",
    "--prodrun",
    action="store_true",
    help="If not set, script will send output to test emails and not the real ones.",
)
parser.add_argument(
    "-v", "--verbose", action="store_true", help="Print verbose debug messages."
)
args = parser.parse_args()

if __name__ == "__main__":
    (IP_Checker(args)).run()
