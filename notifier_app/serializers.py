# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Сериализаторы
"""

from rest_framework import serializers

from notifier_app.models import EmailNotification


class EmailNotificationSerializer(serializers.ModelSerializer):
    """Сериализатор модели EmailNotification
    """

    pk = serializers.UUIDField(read_only=True)
    skipping = serializers.BooleanField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    modified_date = serializers.DateTimeField(read_only=True)
    version = serializers.IntegerField(read_only=True)

    class Meta:
        """Подключение модели которую необходимо сериализовывать
        """

        model = EmailNotification

        fields = [
            'pk',
            'sender',
            'recipient',
            'subject',
            'body',
            'notification_status',
            'sent_date',
            'last_error_date',
            'skipping',
            'created_date',
            'modified_date',
            'version',
        ]


if __name__ == '__main__':
    pass
