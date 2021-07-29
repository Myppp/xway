import requests


def test_get_info_categories(login):
    """"Проверка GET запроса метода /export-system-settings/marketplace/{id}/get-info-categories/"""
    headers = {  'Cookie': 'csrftoken=O5NAWS0AyfuH81T17Ug8ynPP2jsZtlsywPhWJXHHmZIQyMoTLk3KQn77nOcFtinx; sessionid=6ci2kg843pfarkaamnn3y4tafskx8c9u'}
    result = requests.get(url='http://dev3.aliway.ru/export-system-settings/marketplace/1/get-info-categories/', header=login)
    print(login)
    assert result.status_code == 200
