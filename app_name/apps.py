# encoding: utf-8

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):
    """
    {{ app_name }} application
    """
    name = '{{ app_name }}'

    def ready(self):
        pass
