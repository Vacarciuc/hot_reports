from object import DataCollector
import requests
import json

url = "localhost:0000"

def send_data(dataColector: DataCollector):

    payload = dataColector

    response = requests.post(url, data = payload)

    if response.status_code == 200:
        return True
    else:
        return False