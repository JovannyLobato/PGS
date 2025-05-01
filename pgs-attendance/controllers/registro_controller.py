from dao.kid_dao import find_kid_by_fingerprint
from dao.registro_dao import registrar_entrada

def procesar_huella(fingerprint_hash):
    kid = find_kid_by_fingerprint(fingerprint_hash)
    if kid:
        registrar_entrada(kid.id)
        return f"Entrada registrada para: {kid.name}"
    else:
        return "No se encontró ninguna coincidencia de huella"

