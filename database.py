import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",  #pongan su usuario
            password="rammus", #pongan su password
            database="registro_huellas"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def ejecutar_query(self, query, params=None):
        """Ejecuta una consulta SQL y devuelve los resultados."""
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def ejecutar_modificacion(self, query, params=None):
        """Ejecuta una consulta SQL que modifica la base de datos (INSERT, UPDATE, DELETE)."""
        self.cursor.execute(query, params or ())
        self.conn.commit()
    
    def cerrar_conexion(self):
        """Cierra la conexión con la base de datos."""
        self.cursor.close()
        self.conn.close()
