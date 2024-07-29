import pandas as pd
import numpy as np
import pprint
'''
24.07.29 Rich Notification 규약(Depth)과 예시 확인하여 작성
'''
##### INPUT
df = pd.read_csv(r'D:\2022\Python\pandas\pandas_json\weather_data.csv')
#######################################################################

def input_col(text1):
    col_dict = {"bgcolor":"#ffffff",
                    "border": True,
                    "align":"Center",
                    "valign":"middle",
                    "type":"label",
                    "control": {
                        "active":True,
                        "text":[text1, "", "", "", ""],
                        "color":""
                    }}    
    return col_dict

def single_row(cols_list):
    row_dict = {"bgcolor":"#ffffff",
                "border": False,
                "align":"",
                "width":"", 
                "column":cols_list}
    return row_dict  
    
def input_rows(rows_list):
    final_dict = {"row": rows_list}
    return final_dict


titles = [input_col(title) for title in list(df.columns)]
rows = []
for idx in range(df.shape[0]): # no title day, temp, condition
    cols = [input_col(row) for row in df.iloc[idx].values.flatten().tolist()]
    row = single_row(cols)
    rows.append(row)

header_row = single_row(titles)
rows.insert(0, header_row)  # 헤더를 첫 번째로 추가
final_dict = input_rows(rows)
print(len(final_dict['row']))
print(final_dict)

'''
{'row': [{'bgcolor': '#ffffff', 'border': False, 'align': '', 'width': ''
, 'column': [{'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['day', '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['temp', '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['condition', '', '', '', ''], 'color': ''}}]}, {'bgcolor': '#ffffff', 'border': False, 'align': '', 'width': '', 'column': [{'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Monday', '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': [12, '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Sunny', '', '', '', ''], 'color': ''}}]}, {'bgcolor': '#ffffff', 'border': False, 'align': '', 'width': '', 'column': [{'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Tuesday', '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': [14, '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Rain', '', '', '', ''], 'color': ''}}]}, {'bgcolor': '#ffffff', 'border': False, 'align': '', 'width': '', 'column': [{'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Wednesday', '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': [15, '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Rain', '', '', '', ''], 'color': ''}}]}, {'bgcolor': '#ffffff', 'border': False, 'align': '', 'width': '', 'column': [{'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Thursday', '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': [14, '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Cloudy', '', '', '', ''], 'color': ''}}]}, {'bgcolor': '#ffffff', 'border': False, 'align': '', 'width': '', 'column': [{'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Friday', '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': [21, '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Sunny', '', '', '', ''], 'color': ''}}]}, {'bgcolor': '#ffffff', 'border': False, 'align': '', 'width': '', 'column': [{'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Saturday', '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': [22, '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Sunny', '', '', '', ''], 'color': ''}}]}, {'bgcolor': '#ffffff', 'border': False, 'align': '', 'width': '', 'column': [{'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Sunday', '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': [24, '', '', '', ''], 'color': ''}}, {'bgcolor': '#ffffff', 'border': True, 'align': 'Center', 'valign': 'middle', 'type': 'label', 'control': {'active': True, 'text': ['Sunny', '', '', '', ''], 'color': ''}}]}]} 


'''