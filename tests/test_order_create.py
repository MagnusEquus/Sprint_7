import pytest
import requests
import data
import json
import allure


class TestCreateOrder:

    @allure.title('Проверяем что заказ создается с разными цветами')
    @allure.description('Создаем заказ, параметаризацией передаем разные цвета, смотрим код ответа и что в нем есть поле track')
    @pytest.mark.parametrize("colour", [
        ['BLACK', 'GREY'],
        ['BLACK'],
        []
    ])
    def test_create_order(self, colour):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": colour
        }
        response = requests.post(data.url_create_order, data=json.dumps(payload))
        assert response.status_code == 201 and response.json()["track"]
