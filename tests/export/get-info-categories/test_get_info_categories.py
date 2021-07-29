import pytest
import requests


def test_get_info_categories():
    """"Проверка GET запроса метода /export-system-settings/marketplace/{id}/get-info-categories/"""
    headers = {'Cookie': 'csrftoken=86cmn5yC9kN8mquBNSyozc4IJaKiDK1CcCuUHGC3oIych4CSmWAIV09J6cK7cuGz; sessionid=ngh9p3idu26dfg4rq762f6oh2mtaqrvn'}
    result = requests.get(url='http://dev3.aliway.ru/export-system-settings/marketplace/1/get-info-categories/', headers=headers)

    assert result.status_code == 200