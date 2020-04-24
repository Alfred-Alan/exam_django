from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from .models import *
from hashlib import md5


# Create your views here.
def makepassword(psd):
    return md5(str(psd).encode(encoding="utf-8")).hexdigest()


class Register(APIView):
    def get(self, request):
        # 获取参数
        username = request.GET.get('username', None)
        password = request.GET.get('password', None)
        # 用户验证
        user = User.objects.filter(username=username).first()
        if user:
            return Response({"code": 403, "msg": "该用户已存在"})
        # 添加操作
        try:
            User(username=username, password=makepassword(password)).save()
        except Exception as e:
            print(e)
            return Response({"code": 403, "msg": "注册失败"})

        return Response({"code": 200, "msg": "注册成功"})


class Login(APIView):
    def get(self, request):
        # 获取参数
        username = request.GET.get('username', None)
        password = request.GET.get('password', None)
        print(username, password)
        # 查询操作
        user = User.objects.filter(username=username, password=makepassword(password))
        if user:
            return Response({"code": 200, "msg": "登录成功"})
        else:
            return Response({"code": 403, "msg": "登录失败 用户名或者密码错误"})
