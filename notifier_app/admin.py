# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Панель администратора
"""

from django.contrib import admin

from notifier_app.models import EmailNotification


class EmainNotficationAdmin(admin.ModelAdmin):
    """Отображение модели EmailNotification в панели администратора
    """

    list_display = (
        'id',
        'sender',
        'recipient',
        'subject',
        'notification_status',
        'last_error_date',
        'skipping',
        'created_date',
        'modified_date',
        'version',
    )

    list_display_links = (
        'id',
    )

    search_fields = (
        'id',
        'sender',
        'recipient',
        'subject',
    )

    list_editable = (
        'notification_status',
        'skipping',
    )

    list_filter = (
        'recipient',
        'subject',
        'notification_status',
        'skipping',
    )


admin.site.register(EmailNotification, EmainNotficationAdmin)
