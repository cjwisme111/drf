# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response

from api.throttling import MyThrottle
class TestThrottling(APIView):

    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return Response({
            "status":0,
            "msg" : "get mobile ok"
        })