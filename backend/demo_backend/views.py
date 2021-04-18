# -*- coding: utf-8 -*-

from django.views.decorators.cache import never_cache
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheck(APIView):
    """
    Provides endpoint check for services like Pingdom and clients using the API
    """

    @never_cache
    def get(self, request, *args, **kwargs):
        return Response({
            'msg': 'OK',
            'status': 200,
        })


class DemoEndpoint(APIView):
    """
    Returns a simple message
    """

    def get(self, request, *args, **kwargs):
        return Response({
            'msg': "Hello, you've reached the backend server",
        })
