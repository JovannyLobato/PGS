from dao.kid_dao import get_all_kids
from dao.registro_dao import registrar_entrada
from utils.fingerprint_utils import process_fingerprint, verify_fingerprint


def procesar_huella(fingerprint: str) -> str:
    # Se obtienen todos los niños registrados
    kids = get_all_kids()
    for kid in kids:
        if verify_fingerprint(fingerprint, kid.fingerprint_hash):
            registrar_entrada(kid.id)
            return f"Entrada registrada para: {kid.name}"
    return "No se encontró ninguna coincidencia de huella. Intenta nuevamente."

"""
def procesar_huella(fingerprint_hash):
    kid = find_kid_by_fingerprint(fingerprint_hash)
    if kid:
        registrar_entrada(kid.id)
        return f"Entrada registrada para: {kid.name}"
    else:
        return "No se encontró ninguna coincidencia de huella"
"""
