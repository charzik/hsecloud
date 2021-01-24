import socket

from django.apps import AppConfig


class HandlersConfig(AppConfig):
    name = 'handlers'

    def ready(self):
        from . import models
        try:
            models.Item.objects.update_or_create(
                ip=socket.gethostname(), 
                status='AVAILABLE'
            )
        except Exception:
            return
