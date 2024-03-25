# Proyecto 6

## Pruebas del parámetro "name" en la solicitud de creación de un kit en la aplicación Urban Grocers.

Comprobación del parámetro "name"  hecha a través de 9 pruebas. (5 pruebas positivas y 4 pruebas negativas).
La totalidad de las pruebas se hicieorn en Pycharm, lenguaje Python.
Para la creación del kit se utilizó el método POST (documentación API)

### Las pruebas positivas  (1,2,5,6,7)
El resultado esperado debe ser la creacion exitosa del kit, con un código de respuesta 201.
### Las pruebas negativas (3,4,8,9)
El resultado esperado muestra un error bad request, con un código de respuesta 400.

Para más información consultar la documentación completa API Docs, "/docs/" en la sección: "Main.Kits Crear un Kit"
"/api/v1/kits/"


## Precondiciones para la realización de las pruebas:
1.Tener instalados los paquetes: pytest y requests en Pycharm
2.En el archivo configuration.py actualizar "URL SERVICE" con la dirección del servidor.

## Ejecución de las pruebas
1. En la terminal ejecutar el siguiente comando: pytest create_kit_name_kit_test.py

## Resultados Reales:
De las 9 pruebas, 5 pruebas aprobaron (1,2,5,6,7,) y 4 pruebas no aprobaron (3,4,8,9)
El 55.56% de pruebas aprobaron y el 44.44 % no aprobaron
Las pruebas que no aprobaron la comprobacion estan relacionadas al código 400, ya que el resultado actual 
muestra un código 201, es decir la creacion exitosa del kit con parámetros no permitidos en el campo "name".

======================================================================== short test summary info ========================================================================
FAILED create_kit_name_kit_test.py::test_3_null_character_in_name_get_error_response - assert 201 == 400
FAILED create_kit_name_kit_test.py::test_4_512_character_in_name_get_error_response - assert 201 == 400
FAILED create_kit_name_kit_test.py::test_8_no_name_in_body_get_error_response - assert 201 == 400
FAILED create_kit_name_kit_test.py::test_9_number_boolean_get_error_response - assert 201 == 400



