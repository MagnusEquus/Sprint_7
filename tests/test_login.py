import pytest
import requests
import data
import allure


class TestLogin:

    @allure.title('Проверяем успешный логин')
    @allure.description('Логинимся, проверяем статус код и что передается айди')
    def test_auth(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }
        response = requests.post(data.url_login, data=payload)
        assert response.status_code == 200 and response.json()["id"]

    @allure.title('Проверяем что нельзя залогинится не передав поля')
    @allure.description('Отправляем логин без полей, проверяем код ответа, у 504 сообщнения нет')
    def test_login_without_fields(self, courier):
        response = requests.post(data.url_login)
        assert response.status_code == 504

    @allure.title('Логинимся под несуществующим пользователем')
    @allure.description('Делаем проверку логина, но не создаем перед этим пользователя, проверяем код и сообщение ошибки')
    def test_login_wrong_creds(self, clear_courier):
        payload = {
            "login": data.login,
            "password": data.password
        }
        response = requests.post(data.url_login, data=payload)
        assert response.status_code == 404 and response.json()["message"] == data.response_login_not_found

    @allure.title('Логинимся не передав обязательное поле')
    @allure.description('Пытаемся залогинится не передав пароль, проверяем код ответа, у 504 сообщнения нет')
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
        assert response.status_code == 404  and response.json()["message"] == data.response_login_not_found
