# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import  Response

from api import models, serializers
# 工具视图


# 继承APIView,需要手动调用模型,
# 1. 查数据 models.Book.objects.get(pk = pk,is_deleted=False)
# 2. 序列化实例对象 serializers.BookSerializer(book_obj)
# 单查，群查
class V1Book(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            # 单查
            try:
                book_obj = models.Book.objects.get(pk = pk,is_deleted=False)
            except models.Book.DoesNotExist:
                return Response({
                    "status": 1,
                    "msg" : "数据不存在",
                })
            book_data = serializers.BookSerializer(book_obj).data
        else:
            # 群查
            book_list = models.Book.objects.filter(is_deleted=False)
            book_data = serializers.BookSerializer(book_list, many=True).data
        return Response({
            "status": 1,
            "msg": "ok",
            "result": book_data,
        })


    def post(self, request, *args, **kwargs):
        if isinstance(request.data, dict):
            # 单增
            many = False
        elif isinstance(request.data, list):
            # 群增 [{},{}]
            many = True
        else:
            return Response({
                "status": 1,
                "msg": "ok",
            })
        book_ser = serializers.BookSerializer(data=request.data,many=many)
        book_ser.is_valid(raise_exception=True)
        # book_result = book_ser.save()
        return Response({
            "status": 1,
            "msg": "ok",
            # "result": serializers.BookSerializer(book_result, many=many).data,
        })


from rest_framework.generics import GenericAPIView
class V1GenericsBook(GenericAPIView):

    queryset = models.Book.objects.filter(is_deleted=False)
    serializer_class = serializers.BookSerializer

    # get() 方法定义封装在 generics.RetrieveAPIView，ListAPIView
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    # list 方法过程，封装在mixins.ListModelMixin 红
    def list(self,request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            # 单查
            book_obj = self.get_object()
            book_data = self.get_serializer(book_obj).data
        else:
            # 群查
            book_list = self.get_queryset()
            book_data = self.get_serializer(book_list, many=True).data
        return Response({
            "status": 1,
            "msg": "ok",
            "result": book_data,
        })

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, dict):
            # 单增
            many = False
        elif isinstance(request.data, list):
            # 群增 [{},{}]
            many = True
        else:
            return Response({
                "status": 1,
                "msg": "ok",
            })
        book_ser = self.get_serializer(data = request.data,many=many)
        book_ser.is_valid(raise_exception=True)
        book_result = book_ser.save()
        return Response({
            "status": 1,
            "msg": "ok",
            "result": serializers.BookSerializer(book_result, many=many).data,
        })

# 需要自定义get，post,delete,put,patch方法
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
class V2GenericBook(RetrieveModelMixin,ListModelMixin,GenericAPIView):

    queryset = models.Book.objects.filter(is_deleted=False)
    serializer_class = serializers.BookSerializer

    def get(self,request, *args, **kwargs):
        if kwargs.get("pk"):
            return  self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


from rest_framework.generics import CreateAPIView,RetrieveAPIView,ListAPIView,ListCreateAPIView  # 工具视图类
class V3GenericRetrieveBook(RetrieveAPIView):
    queryset = models.Book.objects.filter(is_deleted=False)
    serializer_class = serializers.BookSerializer


class V3GenericListBook(ListAPIView):
    queryset = models.Book.objects.filter(is_deleted=False)
    serializer_class = serializers.BookSerializer


from rest_framework.viewsets import ModelViewSet
class V4BookModelViewSet(ModelViewSet):

    queryset = models.Book.objects.filter(is_deleted=False)
    serializer_class = serializers.BookSerializer

    def get_objs(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_obj_list(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
