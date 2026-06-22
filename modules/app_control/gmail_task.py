import imaplib
import smtplib
import email
from email.mime.text import MIMEText
import webbrowser
import threading
import time


class GmailTask:
    def __init__(self, email_id, app_password):
        self.email_id = email_id
        self.app_password = app_password

        self.stop_reading = False
        self.skip_current = False

    # ================= LOGIN =================
    def login(self):
        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(self.email_id, self.app_password)
            return mail
        except Exception as e:
            print("Login error:", e)
            return None

    # ================= OPEN GMAIL =================
    def open_gmail(self):
        webbrowser.open("https://mail.google.com")

    # ================= FETCH EMAILS =================
    def get_emails(self, criteria="ALL", limit=5):
        mail = self.login()
        if not mail:
            return []

        mail.select("inbox")
        status, data = mail.search(None, criteria)

        mail_ids = data[0].split()
        latest_ids = mail_ids[-limit:]

        emails = []

        for i in reversed(latest_ids):
            status, msg_data = mail.fetch(i, "(RFC822)")
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject = msg["subject"]
            sender = msg["from"]

            emails.append({
                "from": sender,
                "subject": subject
            })

        return emails

    # ================= BASIC COMMANDS =================
    def read_emails(self):
        emails = self.get_emails("ALL")
        if not emails:
            return "Koi mail nahi mila boss."

        result = ""
        for mail in emails:
            result += f"From: {mail['from']}, Subject: {mail['subject']}\n"

        return result

    def unread_emails(self):
        emails = self.get_emails("(UNSEEN)")
        if not emails:
            return "Koi unread mail nahi hai boss."

        return "\n".join([f"{m['from']} - {m['subject']}" for m in emails])

    # ================= SMART IMPORTANT =================
    def is_important(self, subject):
        keywords = ["otp", "urgent", "interview", "job", "alert", "bank", "security"]
        return any(k in subject.lower() for k in keywords)

    def important_emails(self):
        emails = self.get_emails("ALL", 10)
        imp = [m for m in emails if self.is_important(m["subject"])]

        if not imp:
            return "Koi important mail nahi mila boss."

        return "\n".join([f"{m['from']} - {m['subject']}" for m in imp])

    def smart_important(self):
        emails = self.get_emails("UNSEEN", 10)
        imp = [m for m in emails if self.is_important(m["subject"])]

        if not imp:
            return "No urgent mails boss."

        return "\n".join([f"{m['from']} - {m['subject']}" for m in imp])

    # ================= SUMMARY =================
    def get_summary(self):
        emails = self.get_emails("ALL", 5)

        if not emails:
            return "Inbox empty boss."

        return f"Aaj {len(emails)} naye mails aaye hain."

    # ================= SEND MAIL =================
    def send_mail(self, to_email, subject, body):
        try:
            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = self.email_id
            msg["To"] = to_email

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(self.email_id, self.app_password)
            server.send_message(msg)
            server.quit()

            return "Mail bhej diya boss."
        except Exception as e:
            print("Send error:", e)
            return "Mail bhejne me problem aayi boss."

    # ================= VOICE READING =================
    def read_emails_with_voice(self, speaker):
        self.stop_reading = False
        self.skip_current = False

        def reader():
            emails = self.get_emails("ALL", 5)

            for mail in emails:
                if self.stop_reading:
                    speaker.speak("Mail reading stop kar diya boss.")
                    return

                if self.skip_current:
                    self.skip_current = False
                    continue

                speaker.speak(f"From {mail['from']}")
                speaker.speak(f"Subject {mail['subject']}")

                time.sleep(1)

        threading.Thread(target=reader, daemon=True).start()
        return "Boss mail padhna start kar diya."

    def stop_reading_mails(self):
        self.stop_reading = True
        return "Mail reading band kar diya boss."

    def skip_mail(self):
        self.skip_current = True
        return "Next mail pe ja rahe hain boss."

    # ================= REALTIME NOTIFICATION =================
    def watch_inbox(self, speaker):
        last_count = 0

        while True:
            try:
                emails = self.get_emails("UNSEEN", 1)
                if len(emails) > last_count:
                    last_count = len(emails)
                    mail = emails[0]
                    speaker.speak(f"New mail from {mail['from']}")
            except:
                pass

            time.sleep(10)