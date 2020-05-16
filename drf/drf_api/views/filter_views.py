# -*- coding: utf-8 -*-
from rest_framework.generics import ListAPIView

# 过滤器，分页，django-filter

from ..models import Car
from .. import serializers

from rest_framework.filters import SearchFilter,OrderingFilter
from .. import pagination
from .. import filters

# 第三方插件过滤器
from django_filters.rest_framework import DjangoFilterBackend

class CarView(ListAPIView):

    queryset = Car.objects.all()
    serializer_class = serializers.CarModelSerializer

    # 过滤器后端
    # 搜索格式 ?search=..
    # SearchFilter 是根据search 进行查询
    # filter_backends = [SearchFilter,OrderingFilter,filters.MyFilter]
    # filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend]
    search_param = "search"  # 默认查询参数search,
    search_fields = ["name"]  # 根据要查询的字段

    # OrderingFilter
    # 排序格式 ?ordering=..
    ordering_param = "ordering" # 默认查询参数ordering
    ordering_fields = ["price"]
    ordering = "pk"

    # 插件过滤器参数
    # 自定义filterset_class
    filterset_class = filters.CarAutoFilterSet

    # pagination_class = pagination.MyPageNumberPagination
    # pagination_class = pagination.LimitOffsetPagination
    pagination_class = pagination.MyCursorPagination