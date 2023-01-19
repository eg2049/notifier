# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Представления rest_framework.generics
"""

from django.db.models.query import QuerySet
from rest_framework import generics

from notifier_app.models import EmailNotification
from notifier_app.serializers import EmailNotificationSerializer


class EmailNotificationListCreateAPIView(generics.ListCreateAPIView):
    """Представление для обработки запроса 
    на создание инстанса модели EmailNotification 
    и получение списка инстансов модели EmailNotification
    """

    queryset = EmailNotification.objects.all()
    serializer_class = EmailNotificationSerializer
    permission_classes = []

    def get_queryset(self) -> QuerySet:
        """Получение queryset с email-ами которые необходимо отправить

        Returns:
            QuerySet: queryset с инстансами модели EmailNotification которые необходимо отправить
        """

        qs = self.queryset.filter(notification_status='QUEUED', skipping=False)

        return qs


if __name__ == '__main__':
    pass
