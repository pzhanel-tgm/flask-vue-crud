import requests
import json

url = "http://127.0.0.0:8080/todo"
response = requests.get(url)
asJson = response.json

