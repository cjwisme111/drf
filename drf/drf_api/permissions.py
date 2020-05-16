# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission

from django.contrib.auth.models import User
class MyPermssion(BasePermission):
    """定义权限"""
    def has_permission(self, request, view):
        # 游客可以访问 get,head,option 请求
        # 或者必须是合法用户，且用户输入用户组"管理员"人员
        r1 = request.method in ("GET","HEAD","OPTION")
        # 合法用户，并且已经认证
        r2 = request.user and request.user.is_authenticated
        # 查询用户是否属于用户组的 “管理员”
        r3 = request.user.groups.filter(name="管理员").count()

        return r1 or (r2 and r3)