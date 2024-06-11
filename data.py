import allure
import string
import random
import requests
from config import URL, ENDPOINT_LOGIN, ENDPOINT_COURIER


MESSAGE_NEW_COURIER = '{"ok":true}'
MESSAGE_NOT_FOUND = 'Учетная запись не найдена'
MESSAGE_NOT_ENOUGH_FOR_LOG_IN = 'Недостаточно данных для входа'
MESSAGE_NOT_ENOUGH_FOR_CREATE = 'Недостаточно данных для создания учетной записи'
MESSAGE_ERROR_LOGIN = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'


def register_new_courier():
    with allure.step('Создание нового курьера для проведения теста'):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
            }
        return payload


def delete_data_registered_courier(payload):
    with allure.step('Удаление курьера после проведения теста'):
        response = requests.post(f'{URL}{ENDPOINT_LOGIN}', data=payload)
        id_courier = response.json()['id']
        response = requests.delete(f'{URL}{ENDPOINT_COURIER}/{id_courier}')
        assert response.status_code == 200
