import base64

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header

from django.contrib.auth.models import User

class MyAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # auth = get_authorization_header(request)
        # auth = get_authorization_header(request)
        auth = request.META.get("HTTP_AUTHORIZATION",None)
        if not auth:
            # 表示游客
            return None

        auth_list = auth.split()

        # 基本格式认证
        if not ( len(auth_list) == 2 and auth_list[0] == "auth"):
            raise AuthenticationFailed("格式有误")

        if auth_list[1] != "api.abc.xyz":
            raise AuthenticationFailed("认证值有误")

        user = User.objects.get(username="admin")
        # user.check_password()
        return (user,None)