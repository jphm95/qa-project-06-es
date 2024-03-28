import configuration
import data
import requests


# Función para la creación de un usuario
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.auth_token)


# Función para crear un Kit personal.
def post_new_client_kit(kit_body, auth_token):
<<<<<<< HEAD
    # Obtener el token del usuario previamente creado,para la solicitud post  del nuevo kit.
=======
    # Obtener el token del usuario previamente creado,para poder hacer la solicitud post para el nuevo kit.
>>>>>>> 6610fc11b762cb46bc1980020c9fc4f2474d7c63
    headers = {"Authorization": "Bearer" + auth_token}
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)


response = post_new_client_kit(data.kit_body, data.auth_token)
