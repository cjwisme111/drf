# -*- coding: utf-8 -*-

# 自定义 频率组件

from rest_framework.throttling import SimpleRateThrottle

from rest_framework.exceptions import APIException

class MyThrottle(SimpleRateThrottle):

    """
    一分钟内手机短信次数为一次
    """

    scope = "mobile"

    def get_cache_key(self, request, view):

        mobile = request.query_params.get("mobile")
        if not mobile:
            raise APIException("参数错误，请设置mobile")
        cache_format = "throttling_%(user)s_%(mobile)s" % ({"user":self.scope,"mobile":mobile})
        return cache_format