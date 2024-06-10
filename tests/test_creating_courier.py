import allure
import requests
from config import URL, ENDPOINT_COURIER
from data import MESSAGE_NEW_COURIER, MESSAGE_NOT_ENOUGH_FOR_CREATE, MESSAGE_ERROR_LOGIN


class TestPostCourier:

    @allure.title("Успешное создание курьера при заполнении всех полей.")
    def test_create_new_courier(self, payload_for_create_courier):
        response = requests.post(f'{URL}{ENDPOINT_COURIER}', json=payload_for_create_courier)
        assert response.status_code == 201
        assert response.text == MESSAGE_NEW_COURIER

    @allure.title("Нельзя создать двух одинаковых курьеров.")
    def test_cannot_create_two_identical_couriers(self, payload_for_create_courier):
        response = requests.post(f'{URL}{ENDPOINT_COURIER}', json=payload_for_create_courier)
        assert response.status_code == 201
        response = requests.post(f'{URL}{ENDPOINT_COURIER}', json=payload_for_create_courier)
        assert response.status_code == 409
        assert response.text == MESSAGE_ERROR_LOGIN

    @allure.title("Успешное создание курьера при заполнении только обязательных полей.")
    def test_create_new_courier_without_first_name(self, payload_for_create_courier):
        del payload_for_create_courier['firstName']
        response = requests.post(f'{URL}{ENDPOINT_COURIER}', json=payload_for_create_courier)
        assert response.status_code == 201
        assert response.text == MESSAGE_NEW_COURIER

    @allure.title("Нельзя создать курьера без заполнения обязательного поля 'login'.")
    def test_cannot_create_courier_without_login(self):
        payload = {
            "login": "",
            "password": "password",
            "firstName": "first_name"
        }
        response = requests.post(f'{URL}{ENDPOINT_COURIER}', json=payload)
        assert response.status_code == 400
        assert response.json()['message'] == MESSAGE_NOT_ENOUGH_FOR_CREATE

    @allure.title("Нельзя создать курьера без заполнения обязательного поля 'password'.")
    def test_cannot_create_courier_without_password(self):
        payload = {
            "login": "login",
            "password": "",
            "firstName": "first_name"
        }
        response = requests.post(f'{URL}{ENDPOINT_COURIER}', json=payload)
        assert response.status_code == 400
        assert response.json()['message'] == MESSAGE_NOT_ENOUGH_FOR_CREATE
