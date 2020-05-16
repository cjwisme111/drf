# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response

from api.permissions import MyPermssion


class TestPermission(APIView):

    permission_classes = [MyPermssion]

    def get(self, request, *args, **kwargs):
        return Response({"status":0,"msg":"get permissions ok"})

    def post(self, request, *args, **kwargs):
        return Response({"status":0,"msg":"post permissions ok"})