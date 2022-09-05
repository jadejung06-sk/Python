import pandas as pd
import json
# s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
## JsonDecodeError
# e = json.loads(s) # json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
# print(e)
# json_acceptable_string = s.replace("'", "\"")
# print(json_acceptable_string)
# d = json.loads(json_acceptable_string)
# print(d)


pd.set_option('display.max_colwidth', -1)

raw_json = pd.read_csv('./seaborn_pandas_sklearn/seaborn_pandas_plotly/geojson.csv')['features']
print(type(raw_json)) # Series
replaced_json = raw_json.apply(lambda x: x.replace("'", '\"') if "'" in x else x )
print(type(replaced_json[0])) # str
print(json.loads(replaced_json[107])['geometry']['coordinates']) # Correct
# print(replaced_json[11:20].apply(lambda x : json.loads(x))) # json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 107 (char 106)
# print(replaced_json[0:5])