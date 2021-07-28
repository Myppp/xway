import requests
import sys
from collections import defaultdict

url = 'http://dev3.aliway.ru/cabinet/login/'
session = requests.session()
cookies = session.get(url)
headers = session
print(headers)
csrftoken = cookies.cookies.get_dict()
print(cookies.cookies.get_dict())
cred = {'username' : 'admin@test.ru', 'password' : 'admintestru'}
print(cred)
payload = {**cred, **csrftoken}
print(payload)
post = requests.post(url, headers=cookies, json=payload)
print(post.status_code)