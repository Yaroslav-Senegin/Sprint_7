import allure
import requests
import pytest

from endpoints import EndpointsUrl


@allure.suite('Создание заказа')
class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('Параметризированный тест по созданию заказа с разными цветами и без него')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order(self, color):
        payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "ул. Мира, д.1",
            "metroStation": 4,
            "phone": "+7 913 123 45 67",
            "rentTime": 5,
            "deliveryDate": "2024-04-06",
            "comment": "оставить у двери",
            "color": color
        }
        response = requests.post(EndpointsUrl.ORDER, json=payload)
        assert response.status_code == 201 and 'track' in response.text
