#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

from notifier_app.daemons.daemon_launcher import daemon_launcher

try:
    from config import config
except ImportError:
    exit('DO "cp config/config.py.default config/config.py" and fill in the config file!"')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifier.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # запус демонов перед запуском "основного" приложения
    daemon_launcher()

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
