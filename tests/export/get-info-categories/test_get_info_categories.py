import requests


def test_get_info_categories(headers):
    """"Проверка GET запроса метода /export-system-settings/marketplace/{id}/get-info-categories/"""
    result = requests.get(url='http://dev3.aliway.ru/export-system-settings/marketplace/1/get-info-categories/', headers=headers)
    assert result.status_code == 200
