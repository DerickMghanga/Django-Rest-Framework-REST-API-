import requests

endpoint = "http://127.0.0.1:8000/api/products/10/"

get_response = requests.get(endpoint) #API method

print(get_response.json())