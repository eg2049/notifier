from django.apps import AppConfig


class NotifierAppConfig(AppConfig):
    """Конфигурация приложения
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifier_app'
    verbose_name = 'Notifier App'

    def ready(self) -> None:
        """Операции выполняемые после запуска "основного" приложения
        """

        from notifier_app.daemons.daemon_launcher import daemon_launcher

        # запус демонов перед запуском "основного" приложения
        daemon_launcher()

        return super().ready()


if __name__ == '__main__':
    pass
