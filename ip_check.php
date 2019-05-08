<?php
// Because I didn't want to install composer for one fucking script.
require('not-really-vendors/PHPMailer/src/PHPMailer.php');
require('not-really-vendors/PHPMailer/src/SMTP.php');
require('not-really-vendors/PHPMailer/src/POP3.php');
require('not-really-vendors/PHPMailer/src/Exception.php');

require('secrets/Config.php');

class IP_Checker {
    const PREV_IP_FILE_LOC = '/home/minecraft/prev_known_ip';

    const LOG_LOC = "/var/log/ip_checker_logs";
    const SENT_FROM_NAME = "Yukkuri Notifications";
    const SUBJECT_FMT = "[Yukkuricraft] IP Change Detected on %s";
    const BODY_FMT = "Hi nignogs.<br><br>This is an automagically generated email.<br><br>Prev Server IP: %s<br>New Server IP: %s<br><br>Have fun playing, nerds.<br>- RemiBot";

    const EMAIL_RECIPIENT_FMT = "%s <%s>";

    static function implodeRecipients() {
        $size = sizeof(Config::EMAILS_TO_SEND_TO);

        if ($size >= 1) {
            $recipients = [];
            foreach(Config::EMAILS_TO_SEND_TO as $name => $email) {
                 $recipients[] = sprintf(self::EMAIL_RECIPIENT_FMT, $name, $email);
            }
            if ($size === 1) {
                $string = $recipients[0];
            } else {
                $all_but_last = array_slice($recipients, 0, $size-1);
                $string = implode(", ", $all_but_last);
                $string .= " and ".$recipients[$size-1];
            }
        } else {
            $string = "<No Emails Found>";
        }
        return $string;
    }

    static function writeIpToFile(string $ip) {
        $f = fopen(self::PREV_IP_FILE_LOC, 'w');
        fwrite($f, $ip);
        fclose($f);
    }

    static function log(string $msg) {
        $prepend = sprintf("[%s] ", date('c'));
        error_log($prepend.$msg."\n", 3, self::LOG_LOC);
        var_dump($prepend.$msg);
    }

    /** Idk why I'm writing docblocks
     *
     */
    static function run(bool $test_run = false) {
        $curr_ip = trim(`curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//'`);
        if ( ! is_file(self::PREV_IP_FILE_LOC)) {
            self::writeIpToFile($curr_ip);
        }
        $prev_ip = file_get_contents(self::PREV_IP_FILE_LOC);

        if ($prev_ip !== $curr_ip || $test_run) {
            // IP has changed
            $recipients = self::implodeRecipients();
            if (self::sendMail(sprintf(self::BODY_FMT, $prev_ip, $curr_ip))) {;
                $log_msg = "Sent email to $recipients notifying IP change from $prev_ip => $curr_ip";

                self::writeIpToFile($curr_ip);
            } else {
                $log_msg = "Failed to send email to $recipients";
            }
        } else {
            $log_msg = "IP was detected as not having changed from $prev_ip";
        }

        self::log($log_msg);
    }

    /** ONLY TAKES A MESSAGE BODY
     *
     */
    static function sendMail(string $body) {
        try {
            $mail=new PHPMailer\PHPMailer\PHPMailer();
            $mail->CharSet = 'UTF-8';

            $mail->IsSMTP();
            $mail->Host       = 'smtp.gmail.com';

            $mail->SMTPSecure = 'tls';
            $mail->Port       = 587;
            $mail->SMTPDebug  = 1;
            $mail->SMTPAuth   = true;

            $mail->Username   = Config::THROWAWAY_GMAIL_EMAIL;
            $mail->Password   = Config::THROWAWAY_GMAIL_PASS;

            $mail->SetFrom(Config::THROWAWAY_GMAIL_EMAIL, self::SENT_FROM_NAME);
            $mail->AddReplyTo(Config::REPLY_TO_EMAIL, self::SENT_FROM_NAME);
            $mail->Subject    = sprintf(self::SUBJECT_FMT, date('c'));
            $mail->MsgHTML($body);

            foreach (Config::EMAILS_TO_SEND_TO as $recipient_name => $email) {
                $mail->AddAddress($email, $recipient_name);
            }

            $resp = $mail->send();
            return true;
        } catch (Exception $e) {
            return false;
        }
    }

}

if (sizeof($argv) > 1 && $argv[1] === "-t") {
    $test_run = true;
} else {
    $test_run = false;
}
IP_Checker::run($test_run);

?>
