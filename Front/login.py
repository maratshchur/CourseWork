from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QApplication, QVBoxLayout
import sys
from urls import BASE_URL
import requests 

class LoginForm(QDialog):
    def __init__(self):
        super().__init__()

        self.username_label = QLabel("Username:", self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.login_button = QPushButton("Login", self)

        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

        self.setWindowTitle("Login")
        self.resize(300, 200)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        response = requests.post(f'{BASE_URL}/login', data={'username': username, 'password': password})
        if response.get('success'):
            # Успешная авторизация
            pass
        else:
            print(response.get('message'))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    registration_form = LoginForm()
    registration_form.show()
    sys.exit(app.exec_())