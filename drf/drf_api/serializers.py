# -*- coding: utf-8 -*-
from django.conf import settings

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models

class BookListSerializer(serializers.ListSerializer):

    def update(self, instance, validated_data):
        return [
            self.child.update(instance[index],attrs) for index,attrs in enumerate(validated_data)
        ]

class BookSerializer(serializers.ModelSerializer):

    serializers.SerializerMethodField

    class Meta:
        model = models.Book
        fields = ("id","name","price","img","publish","authors","publish_name","author_list")
        list_serializer_class = BookListSerializer
        extra_kwargs = {
            "id":{
                "read_only": True,
            },
            "publish":{
                "write_only":True
            },
            "authors": {
                "write_only": True
            },
            "publish_name": {
                "read_only": True
            },
            "author_list": {
                "read_only": True
            },
        }
        # depth = 1 # 往下深度一层

    def validate_name(self,value):
        if "g" in value:
            raise ValidationError("不能包含g")
        return value

    def validate(self, attrs):
        return attrs

from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
import re
from django.contrib.auth.models import User

class JSONWebTokenSerializer(serializers.ModelSerializer):
    """生成token"""

    usr = serializers.CharField(write_only=True)
    pwd = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("pwd","usr","username","email")
        extra_kwargs = {
            "username":{
                "read_only":True,
            },
            "email": {
                "read_only": True,
            }
        }

    def validate(self, attrs):
        usr = attrs.get("usr")
        pwd = attrs.get("pwd")
        print(attrs)
        if not all([usr, pwd]):
            raise ValidationError("缺少参数")
        if re.match(r".+@.+", usr):
            user = User.objects.filter(email=usr).first()
        elif re.match(r"1[3-9][0-9]{9}", usr):
            user = User.objects.filter(mobile=usr).first()
        else:
            user = User.objects.filter(username=usr).first()

        if not (usr or user.is_active):
            raise ValidationError("用户不存在")

        # 生成载荷
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        self.object = {
            "user":user,
            "token": token
        }
        return attrs


from . import models
class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Car
        fields = "__all__"