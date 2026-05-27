import requests

req = requests.get("https://swapi.dev/api/people/2")
print(req.status_code)
print(req.content)

