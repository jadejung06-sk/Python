import pandas as pd
import json
s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
## JsonDecodeError
# e = json.loads(s) # json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
# print(e)
# json_acceptable_string = s.replace("'", "\"")
# print(json_acceptable_string)
# d = json.loads(json_acceptable_string)
# print(d)




# raw_json = pd.read_csv('./seaborn_pandas_sklearn/seaborn_pandas_plotly/geojson.csv')['features']
# print(type(raw_json))
# print(raw_json[0])
# print(type(raw_json[0]))