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
