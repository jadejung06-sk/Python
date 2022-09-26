from PIL import ImageFont, ImageDraw, ImageOps, Image
import os

basepath = './watermark/'
jpgpath_list = os.listdir(basepath)
for jpgpath in jpgpath_list:
    if jpgpath.endswith('jpg'):
        finalpath = basepath + jpgpath
        img = Image.open(finalpath)
        # img=Image.open("D:/Python/watermark/2021-10-25-15-35-48-464.jpg")
        width, height = img.size

        text = "♥"
        font = ImageFont.truetype('C:/Users/jjs06/AppData/Local/Microsoft/Windows/Fonts/NanumGothicCoding.ttf', 100)
        txt=Image.new('L', (width,height))
        print(txt)
        d = ImageDraw.Draw(txt)

        for x, y in zip(range(0,width,width//3), range(0,height,height//3)):
            d.text( (x, y), text,  font=font, fill=255)
            d.text( (x+1000, y), text,  font=font, fill=255)
            d.text( (x+2000, y), text,  font=font, fill=255)
            d.text( (x+3000, y), text,  font=font, fill=255)
            d.text( (x-1000, y), text,  font=font, fill=255)
            d.text( (x-2000, y), text,  font=font, fill=255)
            d.text( (x-3000, y), text,  font=font, fill=255)
            w=txt.rotate(45,  expand=1)
            img.paste( ImageOps.colorize(w, (0,0,0), (000, 255, 255)), (242,60),  w)
            img.show()