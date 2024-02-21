import requests

endpoint = "http://127.0.0.1:8000/api/products/1/"

data = {
    "title": "Hello World",
    "price": 00.00
}

get_response = requests.pu(endpoint, json=data) #API method

print(get_response.json())