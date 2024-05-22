from PySide6.QtWidgets import QApplication, QDialog, QLineEdit,  QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
import sys
import requests
import json
from urls import BASE_URL
from UI.ui_register_dialog import Ui_Dialog

class RegisterPage(QDialog, Ui_Dialog):
    def __init__(self):
        super(RegisterPage, self).__init__()
        self.setupUi(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_button.clicked.connect(self.register)
        self.setModal(True)

    def register(self):
        self.email = self.email_input.text()
        self.username = self.username_input.text()
        self.password = self.password_input.text()
        self.confirm_password = self.confirm_password_input.text()

        # Client-side validation
        if not self.email or not self.username or not self.password or not self.confirm_password:
            QMessageBox.critical(self, "Registration Error", "Please fill in all fields")
            return

        if self.password!= self.confirm_password:
            QMessageBox.critical(self, "Registration Error", "Passwords do not match")
            return

        response = requests.post(f'{BASE_URL}/register', data={'email': self.email, 'username':self.username, 'password1': self.password, 'password2': self.confirm_password})

        if response.status_code == 200:
            self.done(QDialog.Accepted)
            
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

    dialog = RegisterPage()
    dialog.show()
    sys.exit(app.exec())