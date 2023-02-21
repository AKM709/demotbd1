import requests

# Replace with your own API key and endpoint URL
API_KEY = "eaffe3ab3d76fe3edd0ae1afd40ab9c3"
URL = "http://localhost:8080/greeting"

# Make a request with a valid API key
headers = {"X-API-Key": API_KEY}
response = requests.get(URL, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print("Error: " + str(response.status_code))

# Make a request with an invalid API key
headers = {"X-API-Key": "invalid-api-key"}
response = requests.get(URL, headers=headers)
