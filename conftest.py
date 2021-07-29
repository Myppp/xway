import pytest
import requests
import json



""""Метод авторизации, записи токена в сессию"""
url = 'http://dev3.aliway.ru/cabinet/login/'
get_login = requests.get(url)
cookies_full = get_login.cookies.values()
cookies = "','".join(cookies_full)
headerest = ['csrftoken=', cookies]
delimiter = ''
head = delimiter.join(headerest)
header = {'Cookie': head}
payload = {'username': 'admin@test.ru', 'password': 'admintestru', 'csrfmiddlewaretoken': cookies}
s = requests.Session()
auth = s.post(url, headers=header, data=payload)
ttoken = cookies.post(url, headers=header, data=payload)
session_full = auth.cookies.values()
ses = "','".join(session_full)
session_short = ['sessionid=', ses]
session = delimiter.join(session_short)
header = [head, session]
header = '; '.join(header)
session = {'Cookies': header}
print(payload)
print(header)
print(session)

t = requests.post
