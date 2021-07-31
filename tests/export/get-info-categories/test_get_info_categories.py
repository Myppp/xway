import requests


def test_get_info_categories():
    """"Проверка GET запроса метода /export-system-settings/marketplace/{id}/get-info-categories/"""
    headers = {  'Cookie': 'csrftoken=7CqbOzOuXSTAicNV7KkzLH4R3ZtbTrEZeFSOB1dt8CJa8KVu36Zd0pT2eOrPaogN; sessionid=ipmr718cornkqebcej60lxfpnwul8vqd'}
    result = requests.get(url='http://dev3.aliway.ru/export-system-settings/marketplace/1/get-info-categories/', headers=headers)
    assert result.status_code == 200
