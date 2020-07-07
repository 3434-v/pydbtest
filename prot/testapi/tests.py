from django.test import TestCase
import requests
import json

url = 'http://127.0.0.1:8089/testapi/readim'
data = {
    "type": "2",
    "msg": "testsss"
}
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
response = requests.post(url, data=data)
print(response.text)