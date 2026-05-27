import requests
import json

req = requests.get("https://fake-json-api.mock.beeceptor.com/users/1")
print(req.status_code)

# user = req.json()
# print(user)

user1 = '''{"id": 1,"name": "Viola Cole","company": "McKenzie, Howe and Predovic","username": "Lura32","email": "Cordie36@gmail.com","address": "633 W Front Street","zip": "45188-7847","state": "Wisconsin","country": "Guam","phone": "(533) 380-2195","photo": "https://json-server.dev/ai-profiles/1.png"}'''

# user1 = '''{"id": 1, "name": 'Viola Cole', "company": 'McKenzie, Howe and Predovic', "username": 'Lura32', "email": 'Cordie36@gmail.com', "address": '633 W Front Street', "zip": '45188-7847', "state": 'Wisconsin', "country": 'Guam', "phone": '(533) 380-2195', "photo": 'https://json-server.dev/ai-profiles/1.png'}'''
userJSON = json.loads(user1)
print(userJSON)
print(f"Name is ",userJSON["name"])


