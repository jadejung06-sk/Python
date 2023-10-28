'''
패키지 만들기 : A + B = C
정적이미지 (jpg/png) -> 애니메이션(gif) 변환 패키지 작성
glob : files to list, 확장자 활용
PIL : Python Image Library
'''
######
# import glob
# from PIL import Image

# ## 이미지, 결과 생성 경로
# path_in = "D:/2022/Python/inflearn/jpgTogif/images/*.png"
# path_out = "D:/2022/Python/inflearn/jpgTogif/images/result.gif"

# ##### 첫 번째 이미지 & 모든 이미지 리스트 패킹
# # img, *images = [Image.open(f) for f in sorted(glob.glob(path_in))]
# # print(img) # <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x247 at 0x206A79E7820>
# # print(images) ## [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x192 at 0x229B5358400>, <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x203 at 0x229B5358C10>, <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x237 at 0x229B5359240>, <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x188 at 0x229B5359450>, <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x184 at 0x229B53594B0>, <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x214 at 0x229B5359510>, <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x161 at 0x229B5359570>, <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x178 at 0x229B53595D0>, <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x271 at 0x229B5359630>, <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=300x179 at 0x229B5359690>]
# ### 리사이즈 (필요한 경우)
# img, *images = [Image.open(f).resize((320, 240), Image.ANTIALIAS) for f in sorted(glob.glob(path_in))]


# ## 이미지 저장
# img.save(
#     fp = path_out,
#     format = 'GIF',
#     append_images = images,
#     save_all = True,
#     duration = 500,
#     loop = 0 
# )
###########################

######
### Class 변환
import glob
from PIL import Image

class GifConverter:
    def __init__(self, path_in=None, path_out = None, resize = (320, 240)):
        '''
        path_in : path of the original images (ex. 'images/*.png')
        path_out : path of the result image (ex. 'output/outputfile.gif')
        resize : the size of resiging images (ex. (320, 240))
        '''
        
        self.path_in = path_in or './*.png'
        self.path_out = path_out or './output.gif'
        self.resize = resize
        
    def convert_gif(self):
        '''
        converts a single gif image
        '''
        print(self.path_in, self.path_out, self.resize)
        
        img, *images = \
             [Image.open(f).resize((self.resize), Image.LANCZOS) for f in sorted(glob.glob(self.path_in))]
            
            # [Image.open(f).resize((self.resize), Image.ANTIALIAS) for f in sorted(glob.glob(self.path_in))]
                       
        
        try:
            img.save(fp = self.path_out,
                    format = 'GIF',
                    append_images = images, ## unpacking
                    save_all = True,
                    duration = 500,
                    loop = 0)
        except IOError:
            print('Cannot convert!', img)
            

if __name__ == '__main__': ## only for developer
    ## class test
    c = GifConverter('D:/2022/Python/inflearn/package/jpgTogif/images/*.png', 'D:/2022/Python/inflearn/package/jpgTogif/output/result.gif', (320, 240))
    c.convert_gif()
    
    # print(GifConverter.convert_gif.__doc__) ##  converts a single gif image