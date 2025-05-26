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
        self.input_nombre.setPlaceholderText("Nombre (ej. Andre@)")
        layout.addWidget(self.input_nombre)

        self.input_apellidos = QLineEdit()
        self.input_apellidos.setPlaceholderText("Apellidos (ej. GP)")
        layout.addWidget(self.input_apellidos)

        self.input_tutor = QLineEdit()
        self.input_tutor.setPlaceholderText("Padre o Tutor (ej. Araceli GO)")
        layout.addWidget(self.input_tutor)

        self.input_maestro = QLineEdit()
        self.input_maestro.setPlaceholderText("Maestro (ej. Vero)")
        layout.addWidget(self.input_maestro)

        self.input_grado = QLineEdit()
        self.input_grado.setPlaceholderText("Grado y grupo (ej. 33B)")
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

        if not all([self.ruta_imagen, nombre, apellidos, tutor, maestro, grado]):
            QMessageBox.warning(self, "Campos incompletos", "Por favor, llena todos los campos y selecciona una imagen.")
            return

