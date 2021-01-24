import socket

from django.apps import AppConfig


class HandlersConfig(AppConfig):
    name = 'handlers'

    def ready(self):
        from . import models
        models.Item.objects.update_or_create(
            ip=socket.gethostbyname(socket.gethostname()), 
            status='AVAILABLE'
        )
