from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel
from controllers.registro_controller import comparar_con_kids

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PGS - Registro de Entrada")

        self.layout = QVBoxLayout()

        self.label = QLabel("Usa Face ID para registrar:")
        self.layout.addWidget(self.label)

        self.btn_face = QPushButton("Usar imagen local para reconocimiento")
        self.btn_face.clicked.connect(self.usar_imagen_local)
        self.layout.addWidget(self.btn_face)

        self.setLayout(self.layout)

    def usar_imagen_local(self):
        ruta_imagen = "imagenes/yo1.jpg"          
        try:
            resultado = comparar_con_kids(ruta_imagen)
            QMessageBox.information(self, "Resultado", resultado)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo procesar la imagen:\n{str(e)}")


