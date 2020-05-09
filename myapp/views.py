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
import upyun

# 文件操作
class file_move(APIView):
    # 删除
    def delete(self,request):
        filename = request.GET.get('filename')
        print(filename)
        up = upyun.UpYun('mdsave', username='ljq', password='m3QsiAaLhMvB8owYEwdl1l2atviBVF3U')
        # 根据路径删除文件
        up.delete('/%s'%filename)
        return Response({'code':200,'msg':'删除成功'})
    # 移动文件
    def get(self,request):
        move = request.GET.get('move')
        # 获取路径
        print(move)
        up = upyun.UpYun('mdsave', username='ljq', password='m3QsiAaLhMvB8owYEwdl1l2atviBVF3U')
        # 根据路径移动文件
        up.move('/jwt.png', '/kaoshi/jwt.png')
        return Response({'code':200,'msg':'移动成功'})

# 上传又拍云
class Upyun(APIView):
    # 创建文件夹
    def get(self,request):
        dname=request.GET.get('dname')
        print(dname)
        up = upyun.UpYun('mdsave', username='ljq', password='m3QsiAaLhMvB8owYEwdl1l2atviBVF3U')
        # 根据获取的名字创建文件夹
        up.mkdir('/%s'%dname)
        return  Response({"code":200,'msg':'创建成功'})

    #上传文件
    def post(self,request):
        # 获取文件
        file=request.FILES.get('file')

        print(file.name)
        up=upyun.UpYun('mdsave',username='ljq',password='m3QsiAaLhMvB8owYEwdl1l2atviBVF3U')
        # 分块上传
        for chunks in file.chunks():
            up.put('/%s'%file.name,chunks,checksum=True)

        return Response({'code':200,'msg':'上传成功','filename':file.name})


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