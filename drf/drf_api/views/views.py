from rest_framework.views import APIView
from rest_framework.response import Response


from api import models, serializers
# 六大接口
# 单查，群查，单增，整体修改，局部修改，单个删除
# 十大接口
# 群增,群改，群局部改，群删

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

# 单增，群增
class V2Book(APIView):

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

# 单整体改，单群体改
class V3Book(APIView):

    def put(self, request, *args, **kwargs):
        # 整体修改
        pk = kwargs.get("pk")
        request_data = request.data
        old_book_list = []
        update_data = []
        if pk and isinstance(request_data,dict):
            pks = [pk]
            request_data = [ request_data ]
        elif not pk and isinstance(request_data, list):
            # [{id:""},{id:""}]
            pks = [ dic.pop("pk",None) for dic in request_data]
        else:
            return Response({
                "status": 0,
                "msg": "数据有误",
            })
        for index, pk in enumerate(pks):
            try:
                book_obj = models.Book.objects.get(pk=pk, is_deleted=False)
            except:
                continue
            old_book_list.append(book_obj)
            update_data.append(request_data[index])

        book_ser = serializers.BookSerializer(old_book_list, data=update_data,many=True)
        book_ser.is_valid(raise_exception=True)
        new_book_objs = book_ser.save()
        book_data = serializers.BookSerializer(new_book_objs,many=True).data

        return Response({
            "status": 0,
            "msg" : "ok",
            "result" : book_data
        })

# 单个局部修改，群体局部修改
class V4book(APIView):

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        request_data = request.data
        old_book_list = []
        update_data = []
        if pk and isinstance(request_data, dict):
            pks = [pk]
            request_data = [request_data]
        elif not pk and isinstance(request_data, list):
            # [{id:""},{id:""}]
            pks = [dic.pop("pk", None) for dic in request_data]
        else:
            return Response({
                "status": 0,
                "msg": "数据有误",
            })
        if not all(pks):
            return Response({
                "status": 0,
                "msg": "数据有误",
            })
        for index, pk in enumerate(pks):
            try:
                book_obj = models.Book.objects.get(pk=pk, is_deleted=False)
            except:
                continue
            old_book_list.append(book_obj)
            update_data.append(request_data[index])

        book_ser = serializers.BookSerializer(old_book_list, data=update_data, many=True,partial=True)
        book_ser.is_valid(raise_exception=True)
        new_book_objs = book_ser.save()
        book_data = serializers.BookSerializer(new_book_objs, many=True).data

        return Response({
            "status": 0,
            "msg": "ok",
            "result": book_data
        })

class V5book(APIView):

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        pks = request.data or []
        # pk 存在，不存在pks,是单个删除
        if pk and not pks:
            pks.append(pk)
        elif pk and pks:
            return Response({
                "status":1,
                "msg" : "数据有误",
            })
        models.Book.objects.filter(pk__in=pks,is_deleted=False).update(is_deleted=True)
        return Response({
            "status": 0,
            "msg" : "ok"
        })