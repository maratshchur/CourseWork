from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication, QMessageBox,\
    QInputDialog
import sys
import requests
import json
from email_verification import VerifyEmailPage
from urls import BASE_URL

class RegisterPage(QDialog):
    def __init__(self):
        super().__init__()

        self.email_label = QLabel("Email:", self)
        self.email_input = QLineEdit(self)
        self.username_label = QLabel("Username:", self)
        self.username_input = QLineEdit(self)
        
        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirm_password_label = QLabel("Confirm Password:", self)
        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_button = QPushButton("Register", self)

        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.register_button)

        widget = QWidget()
        widget.setLayout(layout)


        self.setModal(True)
        self.setWindowTitle("Registration")
        self.resize(300, 200)
        self.setLayout(layout)
        
    
    def register(self):
        email = self.email_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        # Client-side validation
        if not email or not username or not password or not confirm_password:
            QMessageBox.critical(self, "Registration Error", "Please fill in all fields")
            return

        if password != confirm_password:
            QMessageBox.critical(self, "Registration Error", "Passwords do not match")
            return

        response = requests.post(f'{BASE_URL}/register', data={'email': email, 'username': username, 'password1': password, 'password2': confirm_password})

        if response.status_code==200:
            self.verify_email_page = VerifyEmailPage(email, username)
            self.verify_email_page.show()
            self.close()
        else:
            response_data = response.json().get('errors', 'Unknown error')
            response_data = json.loads(response_data)
            if response_data.get('email'):
                error_message = response_data['email'][0]['message']
            elif response_data.get('username'):
                error_message = response_data['username'][0]['message']
            elif response_data.get('password1'):
                error_message = response_data['password1'][0]['message']
            elif response_data.get('password2'):
                error_message = response_data['password2'][0]['message']
            QMessageBox.critical(self, "Registration Error", error_message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    registration_form = RegisterPage()
    registration_form.show()
    sys.exit(app.exec())