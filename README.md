## pillow_util

模块 pillow_util 用于使用 pillow 模块的简单功能, 对其进行简易封装, 无需对图像学基础有任意理解
当然需要对 像素 有一定的理解, 以便对图片操作时定位图中位置


### 主要功能

主要功能: 打开链接图片, 切图, 合图, 加文字, 放大缩小, 置黑白图 等

### 使用场景

主要用于 后端服务 可能会用到简易的图片处理操作.

### 使用方式

需先安装 pillow 模块, 即可使用
```
pip install pillow
```
要想读取图片链接, 还需要安装:
```
pip install requests
```

例子:


```
# coding: utf-8
# filename: test_pillow_util.py

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# sys.path.append('./')
import pillow_util

def test_pillow_util():
    img_url = "./image1.png"
    img2_url = "./image2.jpg"
    im = pillow_util.open_img_from_file(img_url)
    im2 = pillow_util.open_img_from_file(img2_url)
    im3 = pillow_util.paste_img_circle_shape(im, im2, 100, 150, 60)
    im3 = pillow_util.paste_text(im3, u"paste some text here", 200, 180, fontsize=50, fillcolor='black')
    # im3 = pillow_util.gray_img(im3)
    pillow_util.disp_img(im3)
    pillow_util.save_img(im3, "./out.jpg")
    pillow_util.close_img(im)
    pillow_util.close_img(im3)

if __name__ == "__main__":
    test_pillow_util()
```

