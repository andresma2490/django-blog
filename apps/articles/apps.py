from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    name = 'apps.articles'

    def ready(self):
        from . import signals
