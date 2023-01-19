# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Контроллеры
"""

from django.urls import path

from notifier_app.views import EmailNotificationListCreateAPIView

urlpatterns = [
    path(route='email/',
         view=EmailNotificationListCreateAPIView.as_view(), name='email-list-create'),
]


if __name__ == '__main__':
    pass
