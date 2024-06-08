import allure
import pytest
import requests
from config import URL


class TestPostOrder:

    @allure.title('Успешное создание заказа.')
    @pytest.mark.parametrize(
        'scooter_color',
        (['BLACK'], ['GREY'], ['BLACK', 'GREY'], [])
    )
    def test_create_order_with_choice_of_scooter_color(self, payload_for_order, scooter_color):
        with allure.step(f'Выбран цвет самоката: {scooter_color}'):
            payload_for_order['color'] = scooter_color
            response = requests.post(f'{URL}/api/v1/orders', json=payload_for_order)
            assert response.status_code == 201
            assert 'track' in response.json()


class TestGetOrder:

    @allure.title('Получение списка заказов.')
    def test_get_list_orders(self):
        response = requests.get(f'{URL}/api/v1/orders')
        list_of_orders = response.json()
        assert response.status_code == 200
        assert 'orders' in response.json()
        assert list_of_orders['orders'] != []
