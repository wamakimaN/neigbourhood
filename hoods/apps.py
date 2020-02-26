from django.apps import AppConfig


class HoodsConfig(AppConfig):
    name = 'hoods'

    def ready(self):
        import hoods.signals