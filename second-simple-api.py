import requests
import time

while True:
    # req = requests.get("https://courses.codingforeverybody.com")
    req = requests.get("https://reqres.in")
    print(req.status_code)

    if req.status_code != 200:
        print("Request is not successful")
    time.sleep(3)

