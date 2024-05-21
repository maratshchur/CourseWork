from PySide6.QtWidgets import QApplication, QDialog, QLineEdit,  QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
import sys
import requests
import json
from email_verification import VerifyEmailPage
from urls import BASE_URL
from UI.ui_register_dialog import Ui_Dialog

class RegisterDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(RegisterDialog, self).__init__()
        self.setupUi(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_button.clicked.connect(self.register)
        self.setModal(True)

    def register(self):
        email = self.email_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        # Client-side validation
        if not email or not username or not password or not confirm_password:
            QMessageBox.critical(self, "Registration Error", "Please fill in all fields")
            return

        if password!= confirm_password:
            QMessageBox.critical(self, "Registration Error", "Passwords do not match")
            return

        response = requests.post(f'{BASE_URL}/register', data={'email': email, 'username': username, 'password1': password, 'password2': confirm_password})

        if response.status_code == 200:
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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = RegisterDialog()
    dialog.show()
    sys.exit(app.exec())