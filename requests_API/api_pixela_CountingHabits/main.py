import requests
from datetime import datetime

##### id
#  https://pixe.la/@jadejungtest
USERNAME = "jadejungtest"
TOKEN = ""
GRAPH_ID = "graph123412"
TODAY = datetime.now().strftime("%Y%m%d") # 20220414 


##### input
changed_date = datetime(year = 2022, month=4, day= 13).strftime("%Y%m%d")
###########

##### endpoints
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixela_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{changed_date}"

##### configs
user_params = {"token": TOKEN
, "username": USERNAME
, "agreeTermsOfService":"yes"
, "notMinor":"yes"}
graph_config = {"id": GRAPH_ID,
"name":"drinking_water_graph"
,"unit":"liter"
,"type":"float"
,"color":"sora"}
headers = {
    "X-USER-TOKEN" : TOKEN
}
pixela_data = {"date":TODAY,
"quantity": input("How many liters did you drink today?")}

pixela_changed_data = {
"quantity":"2" }

##### post / put / delete
# https://pixe.la/v1/users/jadejungtest/graphs/graph123412.html
# response = requests.post(url = pixela_endpoint, json = user_params)
# graph = requests.post(url = graph_endpoint, json = graph_config, headers=headers)
graph_point = requests.post(url=pixela_creation_endpoint, json = pixela_data, headers=headers)
# graph_updation = requests.put(url=update_endpoint, json = pixela_changed_data, headers=headers)
# delete_pixel = requests.delete(url=update_endpoint, headers=headers)
# print(graph.text, graph_endpoint)
print(graph_point.text)
# print(delete_pixel.text)
