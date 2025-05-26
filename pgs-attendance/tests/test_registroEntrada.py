# tests/test_registro.py
from models.registro import Registro

def test_registro_creacion():
    r = Registro(kid_id=1, timestamp=None)  # o con datetime.datetime.now()
    assert r.kid_id == 1

