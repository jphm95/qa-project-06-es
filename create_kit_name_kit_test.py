import sender_stand_request
import data


# Función para recibir el token
def get_new_user_token():
    new_user_token = data.auth_token
    return new_user_token


# Función que cambiará el contenido del cuerpo de solicitud en el parametro name.
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# Función de prueba positiva
def positive_assert(kit_body):
    kit_body = get_kit_body(kit_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json() != ""


# Función de prueba negativa
def negative_assert_code_400(kit_body):
    kit_body = get_kit_body(kit_body)
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400
    assert response.json["code"] == 400
    assert response.json["message"] == ("El nombre debe contener sólo letras latino, "
                                        "un espacio y un guión. De 2 a 15 caracteres")


# Prueba 1. El número permitido de caracteres(1)
# E.R. Código de respuesta 201.
def test_1_one_character_in_name_get_succes_response():
    positive_assert(kit_body={"name": "a"})


# Prueba 2. El número máximo permitido de caracteres(511)
# E.R. Código de respuesta 201.
def test_2_511_character_in_name_get_succes_response():
    positive_assert(kit_body={"name": "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                                      "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                      "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                                      "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                      "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                                      "dAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                      "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                                      "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                      "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                                      "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"})


# Prueba 3. El campo nombre se encuentra vacio("")
# E.R. Código de respuesta 400
def test_3_null_character_in_name_get_error_response():
    negative_assert_code_400(kit_body={"name": ""})


# Prueba 4. Se excede el número maximo de caracteres permitidos (512)
# E.R. Código de respuesta 400.
def test_4_512_character_in_name_get_error_response():
    negative_assert_code_400(kit_body={"name": "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                                               "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                               "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                                               "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                               "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                                               "dAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                               "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                                               "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                               "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                                               "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"})


# Prueba 5. Se permiten caracteres especiales en el nombre ("\"Nō%@\",")
# E.R. Código de respuesta 201.
def test_5_special_symbol_in_name_get_succes_response():
    positive_assert(kit_body={"name": "\"Nō%@\","})


# Prueba 6. El nombre del kit permite espacios(A Aaa)
# E.R. Código de respuesta 201.
def test_6_space_in_name_get_succes_response():
    positive_assert(kit_body={"name": "A Aaa"})


# Prueba 7. El nombre del kit permite números(123)
# E.R. Código de respuesta 201.
def test_7_numbers_in_name_get_succes_response():
    positive_assert(kit_body={"name": "123"})


# Prueba 8. El parámetro no se pasa en la solicitud({})
# E.R. Código de respuesta 400
def test_8_no_name_in_body_get_error_response():
    negative_assert_code_400(kit_body={})


# Prueba 9. El parámetro contiene un valor diferente (booleano)()
# E.R. Código de respuesta 400
def test_9_number_boolean_get_error_response():
    negative_assert_code_400(kit_body={"name": 123})
