import allure
import pytest
import helpers
import data


@allure.step('Создаем курьера перед тестом, возвращаем креды, удаляем по завершению')
@pytest.fixture()
def courier():
    list = helpers.register_new_courier_and_return_login_password()
    creds = {
        "login": list.pop(0),
        "password": list.pop(0),
        "firstName": list.pop(0)
    }
    yield creds
    helpers.delete_courier(creds["login"], creds["password"])


@allure.step('Для тестов на создание курьера до и после теста удаляем его из базы')
@pytest.fixture()
def clear_courier():
    helpers.delete_courier(data.login, data.password)
    yield
    helpers.delete_courier(data.login, data.password)

# @pytest.fixture()
# def order():
