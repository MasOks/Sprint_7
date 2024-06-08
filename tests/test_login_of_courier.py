import allure
import pytest
import requests
from config import URL


class TestPostLoginCourier:

    @allure.title("Успешная авторизация зарегистрированного курьера при заполнении всех обязательных полей.")
    def test_courier_authorization_in_system(self, payload_for_create_courier):
        response = requests.post(f'{URL}/api/v1/courier', data=payload_for_create_courier)
        assert response.status_code == 201
        del payload_for_create_courier['firstName']
        response = requests.post(f'{URL}/api/v1/courier/login', json=payload_for_create_courier)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title("Нельзя авторизоваться зарегистрированному курьеру без заполнения обязательных полей.")
    @pytest.mark.parametrize(
        'empty_field',
        ('login', 'password')
    )
    def test_cannot_courier_authorization_with_empty_field(self, payload_for_create_courier, empty_field):
        with allure.step(f'Не заполнено обязательное поле: {empty_field}'):
            response = requests.post(f'{URL}/api/v1/courier', data=payload_for_create_courier)
            assert response.status_code == 201
            del payload_for_create_courier['firstName']
            payload_for_create_courier[empty_field] = ''
            response = requests.post(f'{URL}/api/v1/courier/login', json=payload_for_create_courier)
            assert response.status_code == 400
            assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title("Нельзя авторизоваться курьеру с неправильно указанным обязательным полем.")
    @pytest.mark.parametrize(
        'wrong_data_field',
        ('login', 'password')
    )
    def test_cannot_courier_authorization_with_wrong_data_field(self, payload_for_create_courier, wrong_data_field):
        with allure.step(f'Обязательное поле: {wrong_data_field} заполнено с ошибкой'):
            response = requests.post(f'{URL}/api/v1/courier', data=payload_for_create_courier)
            assert response.status_code == 201
            del payload_for_create_courier['firstName']
            payload_for_create_courier[wrong_data_field] = 'notCorrectData'
            response = requests.post(f'{URL}/api/v1/courier/login', json=payload_for_create_courier)
            assert response.status_code == 404
            assert response.json()['message'] == 'Учетная запись не найдена'
