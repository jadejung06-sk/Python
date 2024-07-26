'''
https://chatgpt.com/
json 모듈을 파이썬으로 사용하고 싶어서 공부하고 싶은데, 
복잡한 형태인데, 
key 중에는 column이랑 row가 있는데 이게 list가 아니라 동일한 key로 반복되는 형태야. 
pandas의 column과 row를 활용해서 json을 만드는 코드 알려줘
'''
{
    "data": [
        {"Name": "Alice", "Age": 30, "City": "New York"},
        {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 35, "City": "Chicago"}
    ]
}

import pandas as pd
import json

# DataFrame 생성
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

# DataFrame을 JSON 형태로 변환
json_data = {
    "data": df.to_dict(orient='records') 
    ## DataFrame을 JSON 호환 리스트 형태로 변환합니다. 
    ## orient='records'는 각 행을 딕셔너리로 변환하여 리스트에 담는 방식입니다.
}

# JSON 문자열로 변환
json_str = json.dumps(json_data, indent=4)

# JSON 출력
print(json_str)

import pandas as pd
import json

# DataFrame 생성
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

# DataFrame을 JSON 형태로 변환
json_data = {
    "data": df.to_dict(orient='records')
}

# JSON 파일에 데이터 저장
with open('data.json', 'w') as file:
    json.dump(json_data, file, indent=4)  ## json.dump()를 사용하여 파이썬 객체를 JSON 파일로 저장합니다

print("Data has been written to data.json")
