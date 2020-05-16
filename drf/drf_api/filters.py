# -*- coding: utf-8 -*-

from rest_framework.filters import BaseFilterBackend



class MyFilter:

    def filter_queryset(self, request, queryset, view):
        return queryset[:2]


from django_filters.filterset import FilterSet
from django_filters import filters
from . import models
class CarAutoFilterSet(FilterSet):

    # 根据自己想要的字段过来,可以区间查询
    price_max = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_min = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = models.Car
        fields = ['brand',"price_min","price_max"]