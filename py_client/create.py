import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "This field is done",
    "price": 5899.99
}

get_response = requests.post(endpoint, json=data) #API method

print(get_response.json())