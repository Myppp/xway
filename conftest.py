import requests


def authorization():
    r = requests.get('http://dev3.aliway.ru/cabinet/login/')
    r.text