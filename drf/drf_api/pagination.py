# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    # 每页的数量
    # ?page=1&page_size=5
    page_size = 3
    # 用户可以自定义每页的数量
    page_size_query_param = "page_size"
    # 用户可以自定义查询每页最大数量值
    max_page_size = 5

from rest_framework.pagination import LimitOffsetPagination
class MyLimitOffsetPagination(LimitOffsetPagination):
    # 格式 ?limit=...&offset=...
    # 去查询的条数
    limit_query_param = 'limit'
    # 偏移起始位置
    offset_query_param = 'offset'
    # 最大条数数量
    max_limit = 5

from rest_framework.pagination import CursorPagination
class MyCursorPagination(CursorPagination):
    # 查询参数 ?cursor=brand
    cursor_query_param = 'cursor'
    # 默认3条
    page_size = 3
    # ordering = '-created'
    # 注： filter_backends中添加了OrderingFilter，会调用OrderingFilter，排序规则必须在视图中定义ordering
    # 反之，用CursorPagination 中默认的ordering
    # 此字段必须存在
    ordering = '-pk'
    # 自定义查询条数 ?page_size=6
    page_size_query_param = "page_size"
    # 自定义查询条数 最大限制条数5
    max_page_size = 5