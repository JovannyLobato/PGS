
import unittest
from unittest.mock import patch, MagicMock
from controllers import registro_controller

class TestProcesarHuella(unittest.TestCase):

    @patch('controllers.registro_controller.get_all_kids')
    @patch('controllers.registro_controller.verify_fingerprint')
    @patch('controllers.registro_controller.registrar_entrada')
    def test_huella_valida(self, mock_registrar, mock_verify, mock_get_kids):
        # Mock de un niño registrado
        mock_kid = MagicMock()
        mock_kid.id = 1
        mock_kid.name = "Juan"
        mock_kid.fingerprint_hash = "hash_valido"

        mock_get_kids.return_value = [mock_kid]
        mock_verify.return_value = True

        result = registro_controller.procesar_huella("hash_valido")
        self.assertEqual(result, "Entrada registrada para: Juan")
        mock_registrar.assert_called_once_with(1)

    @patch('controllers.registro_controller.get_all_kids')
    @patch('controllers.registro_controller.verify_fingerprint')
    def test_huella_invalida(self, mock_verify, mock_get_kids):
        mock_kid = MagicMock()
        mock_kid.fingerprint_hash = "otra_huella"

        mock_get_kids.return_value = [mock_kid]
        mock_verify.return_value = False

        result = registro_controller.procesar_huella("huella_invalida")
        self.assertEqual(result, "No se encontró ninguna coincidencia de huella. Intenta nuevamente.")

    def test_huella_vacia(self):
        result = registro_controller.procesar_huella("")
        self.assertEqual(result, "No se encontró ninguna coincidencia de huella. Intenta nuevamente.")

    def test_huella_malformada(self):
        result = registro_controller.procesar_huella("@@@###")
        self.assertEqual(result, "No se encontró ninguna coincidencia de huella. Intenta nuevamente.")

    def test_huella_larga(self):
        result = registro_controller.procesar_huella("a" * 64)
        self.assertEqual(result, "No se encontró ninguna coincidencia de huella. Intenta nuevamente.")

    def test_huella_minima(self):
        result = registro_controller.procesar_huella("x")
        self.assertEqual(result, "No se encontró ninguna coincidencia de huella. Intenta nuevamente.")

if __name__ == '__main__':
    unittest.main()
