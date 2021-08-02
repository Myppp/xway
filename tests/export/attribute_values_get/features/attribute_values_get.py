# Метод для получения связок значений/характеристик
import requests


def test_get_attribute_values_attribute(headers, url):
    """"Проверка GET запроса метода /export-system-settings/marketplace/<marketplace_id>/ruleset/attribute_values/get/?pim_attribute=<int>
    в качестве marketplace использую AliExpress + pim_attribute"""
    result = requests.get(url=url + 'export-system-settings/marketplace/1/ruleset/attribute_values/get/?pim_attribute=60',
                          headers=headers)
    assert result.status_code == 200


def test_get_attribute_values_value(headers, url):
    """"Проверка GET запроса метода /export-system-settings/marketplace/<marketplace_id>/ruleset/attribute_values/get/?pim_attribute=<int>
    в качестве marketplace использую AliExpress + pim_value"""
    result = requests.get(url=url + 'export-system-settings/marketplace/1/ruleset/attribute_values/get/?pim_value=220',
                          headers=headers)
    assert result.status_code == 200


def test_get_attribute_values_attribute_4xx(headers, url):
    """"Проверка GET запроса метода /export-system-settings/marketplace/<marketplace_id>/ruleset/attribute_values/get/?pim_attribute=<int>
    в качестве marketplace использую AliExpress + pim_attribute"""
    result = requests.get(url=url + 'export-system-settings/marketplace/1/ruleset/attribute_values/get/?pim_attribute=9999',
                          headers=headers)
    assert result.status_code == 422

def test_get_attribute_values_value_4xx(headers, url):
    """"Проверка GET запроса метода /export-system-settings/marketplace/<marketplace_id>/ruleset/attribute_values/get/?pim_attribute=<int>
    в качестве marketplace использую AliExpress + pim_value"""
    result = requests.get(url=url + 'export-system-settings/marketplace/1/ruleset/attribute_values/get/?pim_value=9999',
                          headers=headers)
    assert result.status_code == 422