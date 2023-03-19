# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Демон создания email-ов из событий kafka
"""

from django.db.utils import ProgrammingError

from notifier_app.kafka.consumer import consumer_creator
from notifier_app.models import EmailNotification

from config.config import EMAIL_SENDER


def email_creator_daemon() -> None:
    """Демон создания email-ов из событий kafka
    """

    consumer = None

    while not consumer:

        consumer = consumer_creator(topic='email_notification_topic',
                                    consumer_group_id='email_notification_consumer_group')

    # в msg будет kafka.consumer.fetcher.ConsumerRecord
    for msg in consumer:

        # в атрибуте value будет dict, с данными сообщения
        email = msg.value

        try:
            EmailNotification.objects.create(
                sender=EMAIL_SENDER,
                recipient=email.get('recipient'),
                subject=email.get('subject'),
                body=email.get('url')
            )

        except ProgrammingError:
            pass


if __name__ == '__main__':
    pass
