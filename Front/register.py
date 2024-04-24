from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication, QMessageBox,\
    QInputDialog
import sys
import requests
import json
from urls import BASE_URL
class RegistrationForm(QDialog):
    def __init__(self):
        super().__init__()

        self.email_label = QLabel("Email:", self)
        self.email_input = QLineEdit(self)
        self.username_label = QLabel("Username:", self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.confirm_password_label = QLabel("Confirm Password:", self)
        self.confirm_password_input = QLineEdit(self)
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
        
    def verify_email(self, username):  
        QMessageBox.information(self, "Registration Successful", "Registration successful! Please check your email for the OTP code.")
        otp, ok = QInputDialog.getText(self, "OTP Verification", "Please enter the OTP code:")
        if ok:
            response = requests.post(f'{BASE_URL}/verify-email/{username}', data={'otp_code': otp})
            print(response.json())
            
    def register(self):
        email = self.email_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        response = requests.post(f'{BASE_URL}/register', data={'email':email, 'username': username, 'password1': password, 'password2': confirm_password})

        if response.ok:
            self.verify_email(username)
        else:
            response_data = response.json()['errors']
            
            response_data = json.loads(response_data)
            print(response_data)
            if response_data.get('email'):
                print(response_data['email'][0]['message'])
            elif response_data.get('username'):
                print(response_data['username'][0]['message'])
            elif response_data.get('password1'):
                print(response_data['password1'][0]['message'])
            elif response_data.get('password2'):
                print(response_data['password2'][0]['message'])
              
   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    registration_form = RegistrationForm()
    registration_form.show()
    sys.exit(app.exec_())