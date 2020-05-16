
from django.urls import path

from . import views

from .views import views
from .views import generics_views
from .views import auth_views

# 继承APIView
urlpatterns = [
    path("v1/books/", views.V1Book.as_view()),
    path("v1/books/<pk>/", views.V1Book.as_view()),

    path("v2/books/", views.V2Book.as_view()),
    path("v2/books/<pk>/", views.V2Book.as_view()),

    path("v3/books/", views.V3Book.as_view()),
    path("v3/books/<pk>/", views.V3Book.as_view()),

    path("v4/books/", views.V4book.as_view()),
    path("v4/books/<pk>/", views.V4book.as_view()),

    path("v5/books/", views.V5book.as_view()),
    path("v5/books/<pk>/", views.V5book.as_view()),
]

# 继承GenericsAPIView
urlpatterns += [
    path("v1/generic/books/", generics_views.V1GenericsBook.as_view()),
    path("v1/generic/books/<pk>/", generics_views.V1GenericsBook.as_view()),

# 继承Mixins,GenericsAPIView
    path("v2/generic/books/", generics_views.V2GenericBook.as_view()),
    path("v2/generic/books/<pk>/", generics_views.V2GenericBook.as_view()),

# 继承generics 工具视图类
    path("v3/generic/books/", generics_views.V3GenericListBook.as_view()),
    path("v3/generic/books/<pk>/", generics_views.V3GenericRetrieveBook.as_view()),

# 继承ModelViewSet
    path("v4/generic/books/", generics_views.V4BookModelViewSet.as_view({"get":"get_obj_list"})),
    path("v4/generic/books/<pk>/", generics_views.V4BookModelViewSet.as_view({"get":"get_objs"})),
]

urlpatterns += [
    path("test/", auth_views.TestPermission.as_view()),
]

from .views import throttling_view

urlpatterns += [
    path("test1/", throttling_view.TestThrottling.as_view()),
]

# token 生成
from rest_framework_jwt.views import ObtainJSONWebToken
from .views import jwt_views
urlpatterns += [
    # path("login/", ObtainJSONWebToken.as_view()),
    path("login/", jwt_views.CustmerToken.as_view()),
    path("test/jwt/", jwt_views.JWTTest.as_view()),
]


from .views import filter_views

urlpatterns += [
    path("car/", filter_views.CarView.as_view()),
]

