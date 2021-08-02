# Получение информации по категориям маркетплейса
import requests


def test_get_info_categories_AliExpress(headers, url):
    """"Проверка GET запроса метода /export-system-settings/marketplace/{id}/get-info-categories/
    в качестве marketplace использую AliExpress"""
    result = requests.get(url=url + 'export-system-settings/marketplace/1/get-info-categories/',
                          headers=headers)
    assert result.status_code == 200


def test_get_info_categories_Ozon(headers, url):
    """"Проверка GET запроса метода /export-system-settings/marketplace/{id}/get-info-categories/
    в качестве marketplace использую Ozon"""
    result = requests.get(url=url + 'export-system-settings/marketplace/2/get-info-categories/',
                          headers=headers)
    assert result.status_code == 200


def test_get_info_categories_4xx(headers, url):
    """"Проверка GET запроса метода /export-system-settings/marketplace/{id}/get-info-categories/
    с некорректным идентификатором."""
    result = requests.get(url=url + 'export-system-settings/marketplace/999/get-info-categories/',
                          headers=headers)
    assert result.status_code == 422