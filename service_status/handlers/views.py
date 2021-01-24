import socket

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import DatabaseError

from . import models


@api_view(['GET'])
def healthcheck(request):
    try:
        models.Item.objects.update_or_create(
            ip=socket.gethostname(), 
            status='AVAILABLE'
        )
        items = models.Item.objects.all()
        services = []
        for item in items:
            service = {
                'ip': item.ip,
                'status': item.status
            }
            services.append(service)

        return Response(
            status=200, 
            data={
                'ip': socket.gethostname(), 
                'services': services
            }
        )
    except DatabaseError:
        return Response(
            status=500, 
            data={
                'error': 'Databas is unavalable'
            }
        )
