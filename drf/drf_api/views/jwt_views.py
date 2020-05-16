# -*- coding: utf-8 -*-
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class JWTTest(APIView):

    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return Response({"status":"ok","msg":"校验通过"})

from rest_framework_jwt.views import JSONWebTokenAPIView
from .. import serializers
class CustmerToken(APIView):

    def post(self, request, *args, **kwargs):
        token_ser = serializers.JSONWebTokenSerializer(data=request.data)
        token_ser.is_valid(raise_exception=True)
        user_ser = serializers.JSONWebTokenSerializer(token_ser.object.get("user"))
        return Response({
            "status":0,
            "msg":"ok",
            "result": user_ser.data,
            "token": token_ser.object.get("token")
        })