import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint)  #API method
print(get_response.text)  #print raw text response