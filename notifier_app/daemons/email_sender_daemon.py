# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Демон отправки email-ов
"""

import smtplib
import socket
import time

from datetime import datetime

import requests

from django.core.mail import send_mail

from config.config import LOCAL_HOST_HTTP, SERVICE_PORT


def email_sender_daemon() -> None:
    """Демон отправки email-ов
    """

    while True:

        try:
            not_sent_emails = requests.get(
                url=f'{LOCAL_HOST_HTTP}:{SERVICE_PORT}/api/v1/email/'
            )

            for email in not_sent_emails.json():

                try:
                    sent = send_mail(
                        subject=email.get('subject'),
                        message=email.get('body'),
                        from_email=email.get('sender'),
                        recipient_list=[
                            email.get('recipient')
                        ]
                    )

                    json_body = {
                        'sender': email.get('sender'),
                        'recipient': email.get('recipient'),
                        'subject': email.get('subject'),
                        'body': email.get('body'),

                    }

                    operation_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

                    # проставление email-у статуса и даты отправки, если удалось отправить
                    if sent:
                        json_body['notification_status'] = 'SENT'
                        json_body['sent_date'] = operation_date

                    # проставление email-у даты ошибки, если не удалось отправить
                    else:
                        json_body['notification_status'] = email.get(
                            'notification_status')
                        json_body['last_error_date'] = operation_date

                    response = requests.put(
                        url=f'{LOCAL_HOST_HTTP}:{SERVICE_PORT}/api/v1/email/update/{email.get("pk")}/',
                        json=json_body
                    )

                    if response.status_code != 200:
                        pass

                except smtplib.SMTPSenderRefused as exc:
                    pass

                except socket.gaierror as exc:
                    pass

        except requests.exceptions.ConnectionError:
            pass

        time.sleep(5)


if __name__ == '__main__':
    pass
