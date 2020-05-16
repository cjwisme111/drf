# -*- coding: utf-8 -*-
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import  Response

def exception_handler(exc, context):
    """调用默认"""
    response = drf_exception_handler(exc, context)
    if response is None:
        print("exc:{exc}---view:{view}---args:{args}---kwargs:{kwargs}".format(exc=exc,**context))
        response = Response({
            "detail" : "服务器错误"
        })
    return response