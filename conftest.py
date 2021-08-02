import pytest
import requests


@pytest.fixture(scope='session')
def headers():
    """"Метод авторизации, получаем токен и sessionid"""
    url = 'http://dev3.aliway.ru/cabinet/login/'
    get_login = requests.get(url)
    cookies_full = get_login.cookies.values()
    cookies = "','".join(cookies_full)
    headerest = ['csrftoken=', cookies]
    delimiter = ''
    head = delimiter.join(headerest)
    header = {'Cookie': head}
    payload = {'username': 'admin@test.ru', 'password': 'admintestru', 'csrfmiddlewaretoken': cookies}
    session = requests.Session()
    post_login = session.post(url, headers=header, data=payload)
    session_data = post_login.request.headers
    dict_iter = [s.replace('python-requests/2.26.0', '') for s in session_data.values()]
    headers = {'Cookie': dict_iter[3 - 4]}
    return headers


@pytest.fixture(scope='session')
def url():
    xway = 'http://dev3.aliway.ru/'
    return xway
