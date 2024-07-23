import pytest
import requests
import data
import allure


class TestLogin:

    @allure.title('Проверяем успешный логин')
    @allure.description('Логинимся, проверяем статус код')
    def test_auth(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }
        response = requests.post(data.url_login, data=payload)
        assert response.status_code == 200

    @allure.title('Проверяем что нельзя залогинится не передав поля')
    @allure.description('Отправляем логин без полей, проверяем код ответа')
    def test_login_without_fields(self, courier):
        response = requests.post(data.url_login)
        assert response.status_code == 504

    @allure.title('Логинимся под несуществующим пользователем')
    @allure.description('Делаем проверку логина, но не создаем перед этим пользователя, проверяем код ошибки')
    def test_login_wrong_creds(self):
        payload = {
            "login": data.login,
            "password": data.password
        }
        response = requests.post(data.url_login, data=payload)
        assert response.status_code == 404

    @allure.title('Логинимся не передав обязательное поле')
    @allure.description('Пытаемся залогинится не передав пароль, проверяем код ошибки')
    def test_login_without_field(self, courier):
        payload = {
            "login": courier["login"]
        }
        response = requests.post(data.url_login, data=payload)
        assert response.status_code == 504

    @allure.title('Логинимся с неверным паролем')
    @allure.description('Передаем неверный пароль, проверяем ошибку')
    def test_login_wrong_pass(self, courier):
        payload = {
            "login": courier["login"],
            "password": '1'
        }
        response = requests.post(data.url_login, data=payload)
        assert response.status_code == 404

    @allure.title('Проверяем что при успешном логине передается айди')
    @allure.description('Логинимся, смотрим что в ответе есть поле с айди')
    def test_login_has_id(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }
        response = requests.post(data.url_login, data=payload)
        assert response.json()["id"]
