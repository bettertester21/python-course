import requests

req = requests.get("https://fake-json-api.mock.beeceptor.com/users/1")
print(req.status_code)

user = req.json()
print(user)

print(f"Name is ",user['name'])
