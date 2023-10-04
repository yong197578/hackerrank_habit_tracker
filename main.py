import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "yongchoi"
TOKEN = "adfei34543dheoajd"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# created user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id": "graph1",
    "name": "Hackerrank Graph",
    "unit": "commit",
    "type": "int",
    "color": 'sora'
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# create user
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_post_endpoint = f"{graph_endpoint}/graph1"
today = datetime.now()
# today = datetime(year=2023, month=10, day=4)
# use strftime to modify datetime format
graph_post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Hackerrank did you do today? "),
}

response = requests.post(url=graph_post_endpoint, json=graph_post_config, headers=headers)
print(response.text)
# graph_put_endpoint = f"{graph_endpoint}/graph1/{today.strftime('%Y%m%d')}"
# graph_put_config = {
#     "quantity": "10"
# }
#
# response = requests.put(url=graph_put_endpoint, json=graph_put_config, headers=headers)
# print(response.text)

# graph_delete_endpoint = f"{graph_endpoint}/graph1/{today.strftime('%Y%m%d')}"
#
# response = requests.delete(url=graph_delete_endpoint, headers=headers)
# print(response.text)