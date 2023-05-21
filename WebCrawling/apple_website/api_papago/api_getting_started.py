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
