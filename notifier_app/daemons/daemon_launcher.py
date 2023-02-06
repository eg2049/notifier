# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Запуск демонов
"""

from threading import Thread

from notifier_app.daemons.email_creator_daemon import email_creator_daemon
from notifier_app.daemons.email_sender_daemon import email_sender_daemon


def daemon_launcher() -> None:
    """Запуск демонов сервиса
    """

    daemons = [
        email_creator_daemon,
        email_sender_daemon,
    ]

    for daemon in daemons:
        th = Thread(target=daemon, daemon=True)
        th.start()


if __name__ == '__main__':
    pass
