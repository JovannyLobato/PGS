from views.registro_kid_view import RegistroKidView

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel, QFileDialog
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
        # Botón para registrar un nuevo kid
        self.btn_registrar_kid = QPushButton("Registrar nuevo Kid")
        self.btn_registrar_kid.clicked.connect(self.abrir_registro_kid)
        self.layout.addWidget(self.btn_registrar_kid)
        self.setLayout(self.layout)

    def usar_imagen_local(self):
        ruta_imagen, _ = QFileDialog.getOpenFileName(
            self, "Selecciona una imagen", "", "Imágenes (*.jpg *.png *.jpeg)"
        )

        if not ruta_imagen:
            return  # El usuario canceló

        try:
            resultado = comparar_con_kids(ruta_imagen)
            if resultado:
                QMessageBox.information(self, "Registro exitoso", f"¡Registro exitoso para el ID: {resultado}!")
            else:
                QMessageBox.warning(self, "No reconocido", "No se reconoció ningún rostro.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo procesar la imagen:\n{str(e)}")
    
    def abrir_registro_kid(self):
        self.registro_kid_view = RegistroKidView()
        self.registro_kid_view.show()
