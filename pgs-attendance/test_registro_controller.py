from controllers import registro_controller

def test_comparar_con_kids_sin_rostros():
    resultado = registro_controller.comparar_con_kids("tests/data/sin_rostro.jpg")
    assert resultado == "No se detectó ningún rostro en la imagen."

