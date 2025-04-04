
# asi se instala el framework PyQt y el conector con mysql
# pip install pyqt5 mysql-connector-python


from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingreso por huella")
        self.setFixedSize(300, 200)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Escanea tu huella o ingresa tu ID temporal:")
        layout.addWidget(self.label)

        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("ID del usuario")
        layout.addWidget(self.input_id)

        self.button_login = QPushButton("Verificar")
        self.button_login.clicked.connect(self.verify_user)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

    def verify_user(self):
        user_id = self.input_id.text()
        if user_id == "":
            QMessageBox.warning(self, "Error", "Por favor ingresa un ID o escanea una huella")
        else:
            QMessageBox.information(self, "Acceso", f"Usuario con ID {user_id} verificado (modo prueba)")
