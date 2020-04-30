import uuid

from PIL import Image,ImageDraw,ImageFont
import cv2
from hashlib import md5


def make_img(filename):

    # 打开文件
    img=Image.open(filename)
    # 获取宽高
    width,height=img.size
    text='django2.0.4'
    # 读取字体
    font=ImageFont.truetype('msyh.ttc',(width-height)//10)
    # 获取字体宽高
    font_width,font_height=font.getsize(text)
    # 定义画笔对象
    draw=ImageDraw.Draw(img)
    # 添加水印
    draw.text((width-font_width,height-font_height),text,font=font,fill=(255,255,255))
    filename=str(uuid.uuid4())+'.jpg'
    # 先压缩
    img.save(filename)

make_img('ANTOINE-LAURENT-1.jpg')

