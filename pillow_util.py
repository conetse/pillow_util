# coding: utf-8

# 此工具包用于无脑使用 pillow 模块的简单功能, 对其进行简易封装, 无需对图像学基础有任意理解
# 当然需要对 像素 有一定的理解, 以便对图片操作时定位图中位置
# 主要功能: 打开链接图片, 切图, 合图, 加文字, 放大缩小, 置黑白图 等

import StringIO
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

try:
    import requests
except Exception as e:
    requests = None

font_file = u"font/ms_yahei.ttf"


# 图片上写入文字
def paste_text(im, text, x, y, fontsize=30, fillcolor='black'):
    draw = ImageDraw.Draw(im)
    try:
        myfont = ImageFont.truetype(font_file, size=fontsize)
    except Exception as e:
        myfont = None
    draw.text((x, y), u"%s" % text, font=myfont, fill=fillcolor)
    return im

# 图片上画上方形图
def paste_img_rectange_shape(im, im_head, x, y, rx, ry):
    im_head_resize = im_head.copy().resize((rx, ry))
    box = (x, y, x+rx, y+ry)
    im.paste(im_head_resize, box)
    return im

# 图片上画上圆形图
def paste_img_circle_shape(im, im_head, x, y, radius):
    im_head_resize = im_head.copy().resize((2*radius, 2*radius))
    major = 2*radius
    minor = 2*radius
    x -= radius
    y -= radius

    # create a new image in which to draw the ellipse
    im_ellipse = Image.new('RGBA', (major, major), (255, 255, 255, 0))
    draw_ellipse = ImageDraw.Draw(im_ellipse, "RGBA")
    # draw the ellipse
    ellipse_box = (0, 0, major, minor)
    draw_ellipse.ellipse(ellipse_box, fill='white')

    # paste it into the existing image and return the result
    im.paste(im_head_resize, (x, y, x+major, y+minor), mask=im_ellipse)
    return im

# 从图片中截取一块方形图
def cut_rectange_img(im, x, y, rx, ry):
    box = (x, y, rx, ry)
    region = im.crop(box)
    return region

# 放大缩小图多少倍
def resize_img(im, ratio=1.0):
    sx, sy = im4.size
    _sx = int(float(sx) * float(ratio))
    _sy = int(float(sy) * float(ratio))
    im_new = im.resize((_sx, _sy))
    return im_new

# 把彩色图变成灰色图
def gray_img(im):
    im_gray = im.convert("L")
    return im_gray

# 从图片文件打开图片
def open_img_from_file(filepath):
    im = Image.open(filepath).convert("RGBA")
    return im

# 从图片url打开图片
def open_img_from_url(img_url):
    if not requests:
        return None
    try:
        r = requests.get(img_url, timeout=2.0)
    except Exception as e:
        return None
    im = Image.open(BytesIO(r.content)).convert("RGBA")
    return im

# 关闭打开的图片
def close_img(im):
    if not im:
        return
    try:
        im.close()
    except Exception as e:
        pass

# 返回图像的文件二进制数据
def get_img_filedata(im):
    f = StringIO.StringIO()
    im.convert("RGB").save(f, 'JPEG')
    img_data = f.getvalue()
    return img_data

# 任意格式转换保存, 简化处理
def save_img(im, filename):
    try:
        im.save(filename)
    except Exception as e:
        im.convert("RGB").save(filename)

# 打开窗口展示图片
def disp_img(im):
    im.show()

def test_pillow_util():
    img_url = "./image1.png"
    img2_url = "./image2.jpg"
    im = open_img_from_file(img_url)
    im2 = open_img_from_file(img2_url)
    im3 = paste_img_circle_shape(im, im2, 100, 150, 60)
    im3 = paste_text(im3, u"paste some text here", 200, 180, fontsize=50, fillcolor='black')
    # im3 = gray_img(im3)
    disp_img(im3)
    save_img(im3, "./out.jpg")
    close_img(im)
    close_img(im3)

if __name__ == "__main__":
    test_pillow_util()
