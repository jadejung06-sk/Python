##### naver api
## developer api 
## > application > enroll the application > papago translation service > web > http://localhost
## > papago Documentation > "api reference"
## > Python example
# >>> https://developers.naver.com/main/
# >>> https://developers.naver.com/apps/#/wizard/register
# >>> https://developers.naver.com/docs/papago/README.md
# >>> https://developers.naver.com/docs/papago/papago-nmt-example-code.md#python
'''
web 
http://localhost
<real http address>
<id> <pw>
requests.post https://openapi.naver.com/v1/papago/n2mt
'''

##### ID PW
# D:\2022\Python\gitignore\personal.py
'''
from gitignore.personal import Personal
'''

##### 앰퍼샌드(&) 문자를 사용할 수 없습니다. & 연산자는 나중에 사용하도록 예약되었습니다. 
## 앰퍼샌드를 문자열의 일부로 전달하려면 큰따옴표로 묶으십시오("&").
# '''안녕하세요? 반갑습니다. 저는 지금 파파고를 활용한 번역 프로그램을 만들어 보았습니다. 지금 시도 중이에요.'''
'''
"안녕하세요? 반갑습니다. 저는 지금 파파고를 활용한 번역 프로그램을 만들어 보았습니다. 지금 시도 중이에요."
'''

##### " " json vs. ' ' dict
## AttributeError: 'dict' object has no attribute 'decode' 
# import json
# response_body = response.read()
# response_body = json.loads(response_body)
# response_body.decode('utf-8')
'''
import json
response_body = response.read()
response_body = json.loads(response_body)
response_body['message']['result']['translatedText']
'''

##### change a row of the different column
## No change
# row['korean'] = translate(row['english'])
# >>> https://jimmy-ai.tistory.com/245
'''
data.loc[i, 'korean'] = translate(row['english'])
'''

##### Korean Error
## data.to_csv(r"D:\2022\Python\WebCrawling\apple_website\api_papago\out.csv")
## data.to_csv(r"D:\2022\Python\WebCrawling\apple_website\api_papago\out.csv", encoding= 'utf-8')
'''
data.to_csv(r"D:\2022\Python\WebCrawling\apple_website\api_papago\out.csv", encoding= 'cp949')
'''

##### faster
## than for i, row in data.iterrows()
# >>> https://ltlkodae.tistory.com/10
# for tu in data.itertuples()
# type(tu.korean) # Float
## AttributeError: can't set attribute
# for tu in data.itertuples()
# tu.korean = str(tu.korean)
# print(tu) # Pandas(Index=0, english='Life begins at the end of your comfort zone.', korean=nan)
'''
for tu in data.itertuples():
    data.loc[tu.Index, 'korean']  = translate(tu.english)
'''
'''
for i, a, b in data.itertuples():
    data.loc[i, 'korean']  = translate(a)

'''
