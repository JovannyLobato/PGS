""" 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from controllers.registro_controller import process_fingerprint

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PGS")
        layout = QVBoxLayout()
        
        btn = QPushButton("Simular Huella")
        btn.clicked.connect(self.simular_huella)
        layout.addWidget(btn)
        
        self.setLayout(layout)

    def simular_huella(self):
        # Simulamos una huella fija (deberia de estar hashed)
        resultado = process_fingerprint("abc123")
        QMessageBox.information(self, "Resultado", resultado)
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLineEdit, QLabel
from controllers.registro_controller import procesar_huella

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PGS - Registro de Entrada")

        self.layout = QVBoxLayout()

        self.label = QLabel("Ingresa la huella (texto):")
        self.layout.addWidget(self.label)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        self.btn = QPushButton("Registrar entrada")
        self.btn.clicked.connect(self.simular_huella)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)

    def simular_huella(self):
        huella_texto = self.input_field.text()
        if not huella_texto.strip():
            QMessageBox.warning(self, "Advertencia", "Por favor ingresa un texto para la huella.")
            return

        resultado = procesar_huella(huella_texto)
        QMessageBox.information(self, "Resultado", resultado)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


