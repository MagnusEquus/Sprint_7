import pytest
import requests
import data
import json
import allure

class TestOrderList:

    @allure.title('Проверяем что можно получить список заказов')
    @allure.description('Делаем запрос на список заказов, проверяем код ответа и что список заказов в ответе не пустой')
    def test_get_orders(self):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK"]
        }
        requests.post(data.url_create_order, data=json.dumps(payload))
        response = requests.get(data.url_create_order)
        print(response.json())
        assert response.status_code == 200 and response.json()["orders"]