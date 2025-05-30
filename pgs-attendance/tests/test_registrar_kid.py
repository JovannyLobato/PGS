# tests/test_registrar_kid.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import os
import unittest
from dao.kid_dao import registrar_kid_en_bd
from models.kid import Kid
from config.database import SessionLocal

class TestRegistroKid(unittest.TestCase):

    def setUp(self):
        self.session = SessionLocal()
        self.ruta_valida = 'tests/data/guadalupe.gif'
        self.ruta_sin_rostro = 'tests/data/sin_rostro.jpg'

    def tearDown(self):
        self.session.query(Kid).delete()
        self.session.commit()
        self.session.close()

    def test_registro_exitoso(self):
        exito, mensaje = registrar_kid_en_bd(
            "Juan", "Pérez", "Mamá", "Miss Lucy", "1A", self.ruta_valida
        )
        self.assertTrue(exito)
        self.assertEqual(mensaje, "Niño registrado correctamente")

    def test_falta_datos(self):
        exito, mensaje = registrar_kid_en_bd(
            "", "Pérez", "Mamá", "Miss Lucy", "1A", self.ruta_valida
        )
        self.assertFalse(exito)
        self.assertEqual(mensaje, "Campos incompletos")

    def test_imagen_sin_rostro(self):
        exito, mensaje = registrar_kid_en_bd(
            "Ana", "García", "Papá", "Miss Eva", "2B", self.ruta_sin_rostro
        )
        self.assertFalse(exito)
        self.assertEqual(mensaje, "No se detectó un rostro en la imagen")


