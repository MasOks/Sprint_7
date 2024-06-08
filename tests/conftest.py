import pytest
import random
import data
from faker import Faker
from datetime import datetime, timedelta


@pytest.fixture()
def payload_for_create_courier():
    payload = data.register_new_courier()
    payload_for_delete = {key: value for key, value in payload.items()}
    del payload_for_delete['firstName']
    yield payload
    data.delete_data_registered_courier(payload_for_delete)


@pytest.fixture()
def payload_for_order():
    fake = Faker(locale='ru_RU')
    payload = {
        "firstName": fake.first_name(),
        "lastName":  fake.last_name(),
        "address": fake.address(),
        "metroStation": random.randint(1, 237),
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 7),
        "deliveryDate": str(datetime.now() + timedelta(days=1)),
        "comment": "Звоните в любое время",
        "color": []
    }
    return payload
