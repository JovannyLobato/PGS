from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow
import sys
from config.database import Base, engine
from models.kid import Kid
from models.registro import Registro

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

