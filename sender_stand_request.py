import configuration
import data
import requests


# Función para acceder a la documentación de la API
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


response = get_docs()
print(response.status_code)


# Función para la creación de un usuario
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.auth_token)


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


# Función para crear un Kit personal.
def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=data.auth_token)


response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())


# Función para consultar la tabla kit_model
def get_kits_table():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_TABLE_PATH)


response = get_kits_table()
print(response.status_code)
