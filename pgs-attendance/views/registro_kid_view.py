from models.kid import Kid
from config.database import SessionLocal
import face_recognition
import pickle
from PyQt5.QtWidgets import QMessageBox
from controllers.kid_controller import registrar_kid_con_datos


from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton,
    QFileDialog, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QPixmap


class RegistroKidView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Nuevo Kid")
        self.setFixedSize(400, 600)

        layout = QVBoxLayout()

        # Imagen
        self.label_imagen = QLabel("Haz clic para seleccionar imagen")
        self.label_imagen.setFixedSize(200, 200)
        self.label_imagen.setStyleSheet("border: 1px solid black;")
        self.label_imagen.setScaledContents(True)
        self.label_imagen.mousePressEvent = self.seleccionar_imagen
        layout.addWidget(self.label_imagen)

        # Campos de texto
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre(s)")
        layout.addWidget(self.input_nombre)

        self.input_apellidos = QLineEdit()
        self.input_apellidos.setPlaceholderText("Apellidos")
        layout.addWidget(self.input_apellidos)

        self.input_tutor = QLineEdit()
        self.input_tutor.setPlaceholderText("Padre o Tutor")
        layout.addWidget(self.input_tutor)

        self.input_maestro = QLineEdit()
        self.input_maestro.setPlaceholderText("Maestro")
        layout.addWidget(self.input_maestro)

        self.input_grado = QLineEdit()
        self.input_grado.setPlaceholderText("Grado y grupo")
        layout.addWidget(self.input_grado)

        # Botón para registrar
        self.btn_registrar = QPushButton("Registrar")
        self.btn_registrar.clicked.connect(self.registrar_kid)
        layout.addWidget(self.btn_registrar)

        self.setLayout(layout)

        # Ruta de imagen seleccionada
        self.ruta_imagen = None

    def seleccionar_imagen(self, event):
        ruta, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar imagen", "", "Imágenes (*.png *.jpg *.jpeg *.gif)"
        )
        if ruta:
            self.ruta_imagen = ruta
            pixmap = QPixmap(ruta)
            self.label_imagen.setPixmap(pixmap)

    def registrar_kid(self):
        nombre = self.input_nombre.text()
        apellidos = self.input_apellidos.text()
        tutor = self.input_tutor.text()
        maestro = self.input_maestro.text()
        grado = self.input_grado.text()

        exito, mensaje = registrar_kid_con_datos(
            nombre, apellidos, tutor, maestro, grado, self.ruta_imagen
        )

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.input_nombre.clear()
            self.input_apellidos.clear()
            self.input_tutor.clear()
            self.input_maestro.clear()
            self.input_grado.clear()
            self.label_imagen.clear()
            self.ruta_imagen = None
        else:
            QMessageBox.warning(self, "Error", mensaje)
