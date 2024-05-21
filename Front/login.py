from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QApplication, QVBoxLayout, QMessageBox
from PyQt6.QtCore import QSettings
import sys
from register import RegisterPage
from urls import BASE_URL
import requests 

class LoginPage(QDialog):
    def __init__(self):
        super().__init__()

        self.username_label = QLabel("Email:", self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("Login", self)
        self.register_button = QPushButton("Register", self)

        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.setWindowTitle("Login")
        self.resize(300, 200)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        response = requests.post(f'{BASE_URL}/login', data={'username': username, 'password': password})

        if response.status_code == 200:
            self.session_id = response.json()['session_id']
            # Store the session ID securely
            settings = QSettings('MyCompany', 'MyApp')
            settings.setValue('session_id', self.session_id)
            self.accept()
            QMessageBox.information(self, 'Success',response.json().get('message', 'Successfully verificated'))
            self.close()
            
        else:
            QMessageBox.critical(self, 'Error',response.json().get('error','Unknown error'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = LoginPage()
    login_form.show()
    sys.exit(app.exec())