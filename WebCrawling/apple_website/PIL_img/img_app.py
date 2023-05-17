import os
from PIL import Image
from PIL import ImageFile
##### color vs. gray scale
# img = Image.open(r'D:\2022\Python\WebCrawling\apple_website\PIL_img\1.jpg')
# img = Image.open(r'D:\2022\Python\WebCrawling\apple_website\PIL_img\1.jpg').convert('L')
##### resize vs. thumbnail 
# img.resize((300,500))
# img.thumbnail((300,500))
##### crop
# img = img.crop((50, 50, 150, 150)) # p1(top left), p2(bottom right)  
'''
img = img.crop((50, 50), (150, 150)) # p1(top left), p2(bottom right)  
TypeError: Image.crop() takes from 1 to 2 positional arguments but 3 were given
'''
##### jpeg(quality) to png(quantize)
# img.save(r'D:\2022\Python\WebCrawling\apple_website\PIL_img\new_photo2.jpg', quality = 75)
# img.save(r'D:\2022\Python\WebCrawling\apple_website\PIL_img\new_photo1.jpg', quality = 65, progssive = True) # Faster on the web site
# img.save(r'D:\2022\Python\WebCrawling\apple_website\PIL_img\new_photo1.png')


##### for
ImageFile.LOAD_TRUNCATED_IMAGES = True
path = os.getcwd()
files = os.listdir(path + '/WebCrawling/apple_website/PIL_img')

for file in files:
    img = Image.open(path + '/WebCrawling/apple_website/PIL_img/' + file)
    img.thumbnail((500,2500))
    '''
    img.thumbnail(500,2500)
    x, y = map(math.floor, size)
    TypeError: 'int' object is not iterable
    '''
    img.save(path + '/WebCrawling/apple_website/PIL_img/new_' + file)