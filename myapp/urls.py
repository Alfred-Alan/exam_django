from django.contrib import admin
from django.urls import path
from  .views import *
urlpatterns = [
    # 绑定路由
    path('upload_file/', upload_file.as_view(), name='upload_file')

]
