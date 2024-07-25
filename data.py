login = "test112233"
password = "123123"
firstName = "Test"
password2 = "1111111111111111111"
firstName2 = "Test2"

url = "https://qa-scooter.praktikum-services.ru"
url_login = url + "/api/v1/courier/login"
url_create = url + "/api/v1/courier"
url_delete = url + "/api/v1/courier/"
url_create_order = url + "/api/v1/orders"

response_create_creds_used = "Этот логин уже используется. Попробуйте другой."
response_create_success = {"ok":True}
response_create_without_body = "Недостаточно данных для создания учетной записи"

response_login_without_fields = "Недостаточно данных для входа"
response_login_not_found = "Учетная запись не найдена"
