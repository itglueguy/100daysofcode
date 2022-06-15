

# install this - pip install requests

# just run it with no arguments
import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
print(response.json())


# run it with arguments
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)

json_response = response.json()

# json to dictionary
json_response = json.loads(response.text)

# dict practice
json_response['request']['altitude']