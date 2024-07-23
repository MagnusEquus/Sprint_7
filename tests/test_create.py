import requests
import data
import allure

class TestCreate:

    @allure.title('Проверяем создание курьера')
    @allure.description('Создаем нового курьера по данным, проверяем что код ответа приходит верный')
    def test_create_positive(self, clear_courier):
        payload = {
            "login": data.login,
            "password": data.password,
            "firstName": data.firstName
        }
        response = requests.post(data.url_create, data=payload)
        assert response.status_code == 201

    @allure.title('Проверяем создание двух курьеров')
    @allure.description('Создаем два одинаковых курьера, проверяем что на второго падает ошибка')
    def test_create_2_couriers(self, clear_courier):
        payload = {
            "login": data.login,
            "password": data.password,
            "firstName": data.firstName
        }
        requests.post(data.url_create, data=payload)
        response = requests.post(data.url_create, data=payload)
        assert response.status_code == 409

    @allure.title('Не создается курьер если не передать поля')
    @allure.description('Пытаемся создать курьера без полей')
    def test_create_without_fields(self):
        response = requests.post(data.url_create, data=[])
        assert response.status_code == 400

    @allure.title('Проверяем ответ при создании курьера')
    @allure.description('создаеи курьера, проверяем что у ответа правильное тело')
    def test_create_response(self, clear_courier):
        payload = {
            "login": data.login,
            "password": data.password,
            "firstName": data.firstName
        }
        response = requests.post(data.url_create, data=payload)
        assert response.json() == {"ok":True}

    @allure.title('Проверяем что курьер не создается без одного из обязательных полей')
    @allure.description('Пытаемся создать курьера без пароля, проверяем ошибку')
    def test_create_without_field(self):
        payload = {
            "login": data.login,
            "firstName": data.firstName
        }
        response = requests.post(data.url_create, data=payload)
        assert response.status_code == 400

    @allure.title('Проверяем что нельзя создать пользователя с уже занятым логином')
    @allure.description('создаем двух пользователей, у второго меняем все кроме логина, проверяем ошибку')
    def test_create_same_login(self, clear_courier):
        payload = {
            "login": data.login,
            "password": data.password,
            "firstName": data.firstName
        }
        requests.post(data.url_create, data=payload)
        payload = {
            "login": data.login,
            "password": data.password2,
            "firstName": data.firstName2
        }
        response = requests.post(data.url_create, data=payload)
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

