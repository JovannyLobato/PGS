import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from controllers.registro_controller import procesar_huella

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
        # Simulamos una huella fija (hash o ID que usarías desde el escáner)
        resultado = procesar_huella("abc123hash")
        QMessageBox.information(self, "Resultado", resultado)

