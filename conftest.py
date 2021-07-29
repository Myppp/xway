import requests

""""Метод авторизации, записи токена в сессию"""
url = 'http://dev3.aliway.ru/cabinet/login/'
get_login = requests.get(url)
cookies_full = get_login.cookies.values()
cookies = "','".join(cookies_full)
session = requests.session()
head = session.cookies
headerest = ['csrftoken=', cookies]
delimiter = ''
head = delimiter.join(headerest)
header = {'Cookie': head}
payload = {'username': 'admin@test.ru', 'password': 'admintestru', 'csrfmiddlewaretoken': cookies}
auth = requests.post(url, headers=header, data=payload)
print('Status code: ' + str(auth.status_code))
