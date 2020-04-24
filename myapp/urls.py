from django.contrib import admin
from django.urls import path
from  .views import *
urlpatterns = [
    # 绑定路由
    path('register/', Register.as_view(), name='Register'),
    path('login/', Login.as_view(), name='Login')
]
