from database import Database

db = Database()

# Insertar usuario de prueba
db.ejecutar_modificacion(
    "INSERT INTO usuarios (nombre, apellido, id_huella, fecha_nacimiento, rol) VALUES (%s, %s, %s, %s, %s)",
    ("Juan", "Pérez", "huella123", "2015-06-12", "niño")
)

# Obtener y mostrar usuarios
usuarios = db.ejecutar_query("SELECT * FROM usuarios")
for usuario in usuarios:
    print(usuario)

db.cerrar_conexion()
