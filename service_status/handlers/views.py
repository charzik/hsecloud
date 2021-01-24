import socket

from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import models


@api_view(['GET'])
def healthcheck(request):
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
            'ip': socket.gethostbyname(socket.gethostname()), 
            'services': services
        }
    )

