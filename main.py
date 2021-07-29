import requests


url = "http://dev3.aliway.ru/cabinet/login/"
payload={'username': 'admin@test.ru', 'password': 'admintestru', 'csrfmiddlewaretoken': 'e6xTnwSTXxLBa9sS5Y1AsUQMO72kwuQqnuw5ECcBsqD9Lf9Ez4mrkewvTCt89OKt'}
headers = {'Cookie': 'csrftoken=e6xTnwSTXxLBa9sS5Y1AsUQMO72kwuQqnuw5ECcBsqD9Lf9Ez4mrkewvTCt89OKt'}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.status_code)




import json
import requests


""""Метод авторизации, записи токена в сессию"""
url = 'http://dev3.aliway.ru/cabinet/login/'
get = requests.get(url)
print('Status code: ' + str(get.status_code))
cookies_full = get.cookies.values()
cookies = "','".join(cookies_full)
a = requests.session()
a.get(url)
header = a.cookies
cred = {'username': 'admin@test.ru', 'password': 'admintestru'}
csrfmiddlewaretoken = {'csrfmiddlewaretoken': cookies}
payload = {**cred, **csrfmiddlewaretoken}
headers_tmpl = {'Cookie': cookies}
headerest = ['csrftoken=', cookies]
delimiter = ''
header = delimiter.join(headerest)
headers = {'content-type': 'application/json', 'Cookie': header}
print('headers is ' + str(headers))
print('payload is ' + str(payload))

auth = requests.post(url, headers=dict(headers), json=json.dumps(payload), timeout=30, verify=False)
print('Status code: ' + str(auth.status_code))
