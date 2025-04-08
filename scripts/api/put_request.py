import requests
import json

def put_data(url:str, credentials:tuple):
    path = f'/api/parameters'
    headers = {"Content-Type": "application/json"}
    data = {"component": "1", "component": "2"}
    response = requests.put(url+path, data=json.dumps(data), headers=headers, auth=credentials)
    print(response)

if __name__ == "__main__":
    # Add inputs here
    url = 'https://localhost'
    credentials = ('username', '*****')
    put_data(url, credentials)