from PIL import Image, ImageFont, ImageDraw , ImageOps
import os

##### Fonts and Texts
title_font = ImageFont.truetype('C:/Users/jjs06/AppData/Local/Microsoft/Windows/Fonts/NanumGothicCoding.ttf', 100)
title_text = r"종석 ♥ 영선"
title_width, title_height = title_font.getsize(title_text)
##### Read Images
basepath = './watermark/'
jpgpath_list = os.listdir(basepath)
for jpgpath in jpgpath_list:
    if jpgpath.endswith('jpg'):
        finalpath = basepath + jpgpath
        img = Image.open(finalpath)
        # print(f'Size of Images : {img.size}')
        width, height = img.size # int, int
        # print(f'Types of width, height : {type(width), type(height)}')
        image_editable = ImageDraw.Draw(img)
        img_2 = Image.open(finalpath)
        image_rotated = ImageDraw.Draw(img_2)
        
        width_txt, height_txt = image_editable.textsize(title_text, title_font)
        # print(f'Size of Texts : {image_editable.textsize(title_text, title_font)}')
        for x, y in zip(range(0,width,width//10), range(0,height,height//10)):
            image_editable.text((x, y), title_text, fill=(000, 255, 255), font=title_font)
            # img.rotate(45)
            img.show()


# Size of Images : (2208, 2944)
# Size of Texts : (600, 95)

# Size of Images : (2944, 2208)
# Size of Texts : (600, 95)

# Size of Images : (2560, 1440)
# Size of Texts : (600, 95)