# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Модели
"""

from uuid import uuid4

from django.db import models


class EmailNotification(models.Model):
    """Модель email сообщения
    """

    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False,
                          verbose_name='id записи')

    sender = models.CharField(
        max_length=255, null=False, verbose_name='Отправитель')

    recipient = models.CharField(
        max_length=255, null=False, db_index=True, verbose_name='Получатель')

    subject = models.CharField(
        max_length=255, null=False, verbose_name='Тема письма')

    body = models.TextField(
        blank=True, null=False, db_index=True, verbose_name='Содержание письма')

    notification_status = models.CharField(
        max_length=255, null=False, default='QUEUED', verbose_name='Статус отправки')

    sent_date = models.DateTimeField(
        auto_now_add=False, null=True, verbose_name='Дата отправки')

    last_error_date = models.DateTimeField(
        auto_now_add=False, null=True, verbose_name='Дата ошибки при попытке отправить')

    skipping = models.BooleanField(
        default=False, null=False, verbose_name='Игнорирование отправки')

    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    modified_date = models.DateTimeField(
        auto_now=True, verbose_name='Дата редактирования')

    version = models.PositiveIntegerField(default=0, verbose_name='Версия')

    class Meta:
        """Дополнительные параметры модели
        """

        # определение названия таблицы
        db_table = 'notifier_app_email_notification'

        verbose_name = 'Email сообщение'
        verbose_name_plural = 'Email сообщения'
        ordering = ('created_date', )

    def save(self, *args, **kwargs) -> None:
        """Действия при сохранении инстанса модели
        """

        self.version += 1
        super().save(*args, **kwargs)


if __name__ == '__main__':
    pass
