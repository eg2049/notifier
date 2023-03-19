# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Демон отправки email-ов
"""

import smtplib
import socket

from datetime import datetime
from time import sleep

from django.db.utils import ProgrammingError
from django.core.mail import send_mail

from notifier_app.models import EmailNotification


def email_sender_daemon() -> None:
    """Демон отправки email-ов
    """

    while True:

        try:
            not_sent_emails = EmailNotification.objects.filter(
                notification_status='QUEUED', skipping=False)

            for email in not_sent_emails:

                try:
                    sent = send_mail(
                        subject=email.subject,
                        message=email.body,
                        from_email=email.sender,
                        recipient_list=[
                            email.recipient
                        ]
                    )

                except socket.gaierror as exc:
                    sent = 0

                except smtplib.SMTPSenderRefused as exc:
                    sent = 0

                except smtplib.SMTPAuthenticationError as exs:
                    sent = 0

                finally:

                    operation_date = datetime.now()

                    # проставление email-у статуса и даты отправки, если удалось отправить
                    if sent:
                        email.notification_status = 'SENT'
                        email.sent_date = operation_date

                        email.save()

                    # проставление email-у даты ошибки, если не удалось отправить
                    else:
                        email.last_error_date = operation_date
                        email.save()

        except ProgrammingError:
            pass

        sleep(5)


if __name__ == '__main__':
    pass
