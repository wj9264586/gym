import datetime
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from .auth import LoginAuthentication
from .serializers import StaffInfoSerializer
from .models import *
# 职工信息录入
class AddStaffAPIView(CreateAPIView):
    authentication_classes = [LoginAuthentication]
    serializer_class = StaffInfoSerializer

    def create(self, request, *args, **kwargs):
        # 解析数据
        username = request.data.get("username")
        time = datetime.datetime.now()
        number = time.strftime("%Y%m%d%H%M%S")
        phone = request.data.get("phone")
        sex = int(request.data.get("sex"))
        age = int(request.data.get("age"))
        department = int(request.data.get("department"))
        monthly_pay = request.data.get("monthly_pay")
        data = {
            "username":username,
            "number":number,
            "phone":phone,
            "sex":sex,
            "age":age,
            "department":department,
            "monthly_pay":monthly_pay
        }
        # 实例化序列化器
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if serializer:

            return Response({"msg":"入职信息填写成功","data":serializer.data})
        else:
            return Response({"status":13,"msg":"入职信息填写失败"})
# 查看职工信息
class StaffInfoAPIView(ListAPIView):
    authentication_classes = [LoginAuthentication]
    serializer_class = StaffInfoSerializer
    queryset = StaffUserInfo.objects.all()
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 注销离职人员
class DeleteStaffAPIView(DestroyAPIView):
    authentication_classes = [LoginAuthentication]

    def destroy(self, request, *args, **kwargs):
        number = request.data.get("number")
        user =request.user
        instance = StaffUserInfo.objects.get(number=number)
        if user.authority == 1:
            self.perform_destroy(instance)
            return Response({"msg":"注销成功"})
        else:
            return Response({"status":"14","msg":"权限不够"})



