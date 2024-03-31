import string
import random
import requests

from endpoints import EndpointsUrl

class Helpers:
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_unregistered_courier():
        courier_data = []
        while len(courier_data) != 3:
            courier_data.append(Helpers.generate_random_string(8))
        return courier_data


    def register_new_courier_and_return_login_password():
        login_pass = []
        login = Helpers.generate_random_string(10)
        password = Helpers.generate_random_string(10)
        first_name = Helpers.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(EndpointsUrl.COURIER, data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass


    def new_courier():
        login, password, first_name = Helpers.register_new_courier_and_return_login_password()
        courier = {
            'login': login,
            'password': password
        }
        return courier


    def non_existing_courier():
        resp = requests.post(EndpointsUrl.LOGIN, data=Helpers.new_courier())
        courier_id = resp.json()["id"] + random.randint(1, 999)
        return courier_id
    
    def existing_courier():
        resp = requests.post(EndpointsUrl.LOGIN, data=Helpers.new_courier())
        courier_id = resp.json()["id"]
        return courier_id
