import requests

url = "http://dev3.aliway.ru/cabinet/login/"
response = requests.get(url)
print(response.status_code)
ra = response.cookies.values()
print(ra)

payload={'username': 'admin@test.ru','password': 'admintestru','csrfmiddlewaretoken': 'L1DHf1ahj2w6IX3kwAGPULUKZSeDL7zSAFReEzTX9VWuafO8xG5x8oIdmJBhFs64'}
headers = {'Cookie': 'csrftoken=L1DHf1ahj2w6IX3kwAGPULUKZSeDL7zSAFReEzTX9VWuafO8xG5x8oIdmJBhFs64'}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.status_code)

r = requests.get(url)
ar = r.cookies.values()
print(ar)











import requests

""""Метод авторизации, записи токена в сессию"""
url = 'http://dev3.aliway.ru/cabinet/login/'
session = requests.Session()
cookies = session.get(url)
cred = {'username': 'admin@test.ru', 'password': 'admintestru'}
csrftoken = cookies.cookies.get_dict()
payload = {**cred, **csrftoken}
post = requests.post(url, headers=headers, data=payload)
print(csrftoken)
print(payload)
print(post.status_code)
