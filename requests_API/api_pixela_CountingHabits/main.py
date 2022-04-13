import requests
import datetime

## id
#  https://pixe.la/@jadejungtest
USERNAME = "jadejungtest"
TOKEN = "j0a6d3e4y5y1s8pp3da4"
GRAPH_ID = "graph123412"

## endpoints
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixela_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

## configs
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
pixela_data = {"date":"20220413",
"quantity":"2"}

## post
# https://pixe.la/v1/users/jadejungtest/graphs/graph123412.html
# response = requests.post(url = pixela_endpoint, json = user_params)
graph = requests.post(url = graph_endpoint, json = graph_config, headers=headers)
graph_point = requests.post(url=pixela_creation_endpoint, json = pixela_data, headers=headers)
# print(graph.text, graph_endpoint)
print(graph_point.text)
