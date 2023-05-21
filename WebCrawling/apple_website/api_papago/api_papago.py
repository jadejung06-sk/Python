import json
import os
import sys
import urllib.request
sys.path.append('D:\\2022\\Python') # Only need
from gitignore.personal import Personal


client_id, client_secret = Personal()._get_info("papago_api")

##### input 
input_text = "안녕하세요? 반갑습니다. 저는 지금 파파고를 활용한 번역 프로그램을 만들어 보았습니다. 지금 시도 중이에요."
encText = urllib.parse.quote(input_text)
#########################
##### Korean to English 
data = "source=ko&target=en&text=" + encText
#########################
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
##### Json to dict
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_body = json.loads(response_body)
    # print(response_body.decode('utf-8'))
    print(response_body['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)
#########################

##### English to Korean
input_text = "I've been a Python developer since 2020."
encText = urllib.parse.quote(input_text)
#########################
##### Korean to English 
data = "source=en&target=ko&text=" + encText
#########################
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
##### Json to dict
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_body = json.loads(response_body)
    # print(response_body.decode('utf-8'))
    print(response_body['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)