import requests

""""Метод авторизации, записи токена в сессию"""
url = 'http://dev3.aliway.ru/cabinet/login/'
get = requests.get(url)
cookies = get.cookies.values()
a = requests.session()
a.get(url)
header = a.cookies
se = header.get_dict()
print(se)
cred = {'username': 'admin@test.ru', 'password': 'admintestru'}
csrfmiddlewaretoken = {'csrfmiddlewaretoken': cookies}
payload = {**cred, **csrfmiddlewaretoken}
headers = {'Cookie': cookies}
post = requests.post(url, header=header, data=payload)
print(payload)
print(post.status_code)
