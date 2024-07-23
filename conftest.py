import pytest
import helpers
import data


@pytest.fixture()
def courier():
    list = helpers.register_new_courier_and_return_login_password()
    creds = {
        "login": list.pop(0),
        "password": list.pop(0),
        "firstName": list.pop(0)
    }
    yield creds
    helpers.delete_test_courier(creds["login"], creds["password"])


@pytest.fixture()
def clear_courier():
    helpers.delete_test_courier(data.login, data.password)
    yield True
    helpers.delete_test_courier(data.login, data.password)
