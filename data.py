import string
import random
import requests
from config import URL


def register_new_courier():
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
    response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
    id_courier = response.json()['id']
    response = requests.delete(f'{URL}/api/v1/courier/{id_courier}')
    assert response.status_code == 200
