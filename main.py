#modules
import os
import requests
from datetime import datetime
# keys and endpoints for the project
API_KEY = os.environ.get("API_KEY")
AUTH_KEY = os.environ.get("AUTH_KEY")
today = datetime.now()
sheety_endpoint = os.environ.get("SHEETY")
# asking user for what exercise they have done
user = str(input("What exercise did you do today?"))

nutrinix_endpoint = os.environ.get("END")
resource_params = {
    "query" : user,
}

headers = {
  "x-app-id":API_KEY,
  "x-app-key":AUTH_KEY
}
headers_2 = {
    "Content-Type":"application/json",
    "Authorization": "Bearer 1243567",
}
# posting information of the user to get the information for the exercise the user done
response = requests.post(url=nutrinix_endpoint,json=resource_params,headers=headers)

response.raise_for_status()
excesicse_data = response.json()
print(excesicse_data)
# setting up the google sheets for the information that we have
for data in excesicse_data['exercises']:
    sheety_params = {
        "workout": {
            "date":   today.strftime("%d/%m/%Y"),
            "time":   today.strftime("%I:%M:%S"),
            "exercise": data['name'],
            "duration": data['duration_min'],
            "calories": data['nf_calories']
        }
    }
# and at last posting information to google sheets
response_2 = requests.post(url=sheety_endpoint,json=sheety_params,headers=headers_2)
print(response_2.text)


