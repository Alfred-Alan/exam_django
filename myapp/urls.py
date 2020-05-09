from django.contrib import admin
from django.urls import path
from  .views import *
urlpatterns = [
    # 绑定路由
    path('upload_file/', upload_file.as_view(), name='upload_file'),
    path('upyun/', Upyun.as_view(), name='Upyun'),
    path('file_move/', file_move.as_view(), name='file_move'),

]
