from PIL import Image, ImageFont, ImageDraw , ImageOps
import os

##### Fonts and Texts
title_font = ImageFont.truetype('C:/Users/jjs06/AppData/Local/Microsoft/Windows/Fonts/NanumGothicCoding.ttf', 100)
title_text = r"종석 ♥ 영선"
##### Read Images
basepath = './watermark/'
jpgpath_list = os.listdir(basepath)
for jpgpath in jpgpath_list:
    if jpgpath.endswith('jpg'):
        finalpath = basepath + jpgpath
        img = Image.open(finalpath)
        width, height = img.size
        image_editable = ImageDraw.Draw(img)

        # 6.삽입할 문자의 높이, 너비 정보 가져오기
        width_txt, height_txt = image_editable.textsize(title_text, title_font)

        # 7.워터마크 위치 설정 (margin을 margin_x,margin_y로 나누어서 사용해도 됨)
        margin = 10
        x = width - width_txt - margin
        y = height - height_txt - margin

        # 8.텍스트 적용하기
        image_editable.text((x, y), title_text, fill=(000, 255, 255), font=title_font)
        image_editable.text((15, 15), title_text, fill=(000, 255, 255), font=title_font)
        img.rotate(45)
        img.show()
