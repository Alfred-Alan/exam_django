import uuid

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from .models import *
from hashlib import md5
import os
from django_test.settings import UPLOAD_ROOT
import cv2
from PIL import Image,ImageDraw,ImageFont

# 加水印
def make_img(filename):
    # 打开文件
    img = Image.open(os.path.join(UPLOAD_ROOT,"",filename))
    # 获取宽高
    width, height = img.size
    text = 'django2.0.4'
    # 读取字体
    font = ImageFont.truetype('msyh.ttc', (width - height) // 10)
    # 获取字体宽高
    font_width, font_height = font.getsize(text)
    # 定义画笔对象
    draw = ImageDraw.Draw(img)
    # 添加水印
    draw.text((width - font_width, height - font_height), text, font=font, fill=(255, 255, 255))
    filename = str(uuid.uuid4()) + '.jpg'
    # 保存文件
    img.save(os.path.join(UPLOAD_ROOT,"",filename))
    return filename

def yasuo(filename):
    # 打开图片
    img=cv2.imread(os.path.join(UPLOAD_ROOT,"",filename))
    # 编辑新文件名
    newfilename = str(uuid.uuid4()) + '.jpg'
    # 压缩图片并保存
    cv2.imwrite(os.path.join(UPLOAD_ROOT,"",newfilename),img,[cv2.IMWRITE_JPEG_OPTIMIZE,50])
    # 删除原有图片
    os.remove(os.path.join(UPLOAD_ROOT,"",filename))

    return newfilename

# Create your views here.

class upload_file(APIView):
    def post(self,request):
        myfile=request.FILES.get('file')
        print(myfile.name)
        # 保存文件
        with open(os.path.join(UPLOAD_ROOT,"",myfile.name),'wb')as f:
                for i in myfile.chunks():
                    f.write(i)
        filename=make_img(yasuo(myfile.name))
        # 删除原本文件名
        os.remove(os.path.join(UPLOAD_ROOT,"",myfile.name))

        return Response({'code':200,"img_name":filename})