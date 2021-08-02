# Получение информации по категориям маркетплейса
import requests
from voluptuous import Schema, PREVENT_EXTRA


def test_get_info_categories_schemas(headers, url):
    """ Валидация схемы ручки GET /export-system-settings/marketplace/{id}/get-info-categories/ """
    schema = Schema(
        {
            "data": {
                "all": int,
                "linked": int,
                "unlinked": int,
            },
            "errorMessage": None,
            "isSuccess": bool,
            "marketplace": {
                "code": str,
                "name": str,
            },
            "pagination": None,
        },
        extra=PREVENT_EXTRA,
        required=True
    )

    result = requests.get(url=url + '/export-system-settings/marketplace/2/get-info-categories/', headers=headers).json()

    assert schema == result
