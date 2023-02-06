# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Демон создания email-ов из событий kafka
"""

import requests

from notifier_app.kafka.consumer import consumer_creator

from config.config import EMAIL_SENDER, LOCAL_HOST_HTTP, SERVICE_PORT


def email_creator_daemon() -> None:
    """Демон создания email-ов из событий kafka
    """

    consumer = consumer_creator(topic='email_notification_topic',
                                consumer_group_id='email_notification_consumer_group')

    # в msg будет kafka.consumer.fetcher.ConsumerRecord
    for msg in consumer:

        # в атрибуте value будет dict, с данными сообщения
        email = msg.value

        body = {
            'sender': EMAIL_SENDER,
            'recipient': email.get('recipient'),
            'subject': email.get('subject'),
            'body': email.get('url')
        }

        # демон отправляет запрос к своему же сервису для создания инстанса модели EmailNotification
        response = requests.post(
            url=f'{LOCAL_HOST_HTTP}:{SERVICE_PORT}/api/v1/email/',
            json=body
        )

        if response.status_code != 201:
            pass


if __name__ == '__main__':
    pass
