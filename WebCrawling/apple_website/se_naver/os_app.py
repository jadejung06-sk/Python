import os
import shutil

files = os.listdir(r'D:\2022\Python\WebCrawling\apple_website\se_naver\file_test')

##### rename and copy
# for file in files:
    # os.rename(f'D:/2022/Python/WebCrawling/apple_website/se_naver/file_test/{file}', f'D:/2022/Python/WebCrawling/apple_website/se_naver/file_test/a{file}')
    
# for file in files:
    # shutil.copy(f'D:/2022/Python/WebCrawling/apple_website/se_naver/file_test/{file}', f'D:/2022/Python/WebCrawling/apple_website/se_naver/file_test2/a{file}')
    
##### os.path.join
print(os.path.join(os.getcwd(), 'test')) # D:\2022\Python\test
