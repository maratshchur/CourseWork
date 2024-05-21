from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication, QMessageBox,\
    QInputDialog
from urls import BASE_URL
import requests

class VerifyEmailPage(QDialog):
    def __init__(self, email, username):
        super().__init__()

        self.email = email
        self.username = username

        self.otp_input = QLineEdit()
        self.resend_otp_button = QPushButton("Resend OTP")
        self.resend_otp_button.clicked.connect(lambda: self.resend_otp(email))
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.verify_otp)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Please enter the OTP code:"))
        layout.addWidget(self.otp_input)
        layout.addWidget(self.resend_otp_button)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.setWindowTitle("Verify Email")

    def resend_otp(self, email):
        response = requests.post(f'{BASE_URL}/resend-otp', data={'otp_email': email})

        if response.status_code==200:
            QMessageBox.information(self, 'Succes',response.json().get('message', 'New OTP send'))
        else:
            error_message = response.json().get('error', 'Unknown error')
            QMessageBox.critical(self, "OTP Resent Error", error_message)

    def verify_otp(self):
        from login import LoginPage
        otp = self.otp_input.text()
        response = requests.post(f'{BASE_URL}/verify-email/{self.username}', data={'otp_code': otp})
        if response.status_code == 200:
            QMessageBox.information(self, "OTP Verification", response.json().get('message', 'Successfully verificated'))
            self.login_page = LoginPage()
            self.login_page.show()
            self.close()
            
        elif response.status_code == 401:
            error_message = response.json().get('error', 'Invalid OTP')
            QMessageBox.critical(self, "OTP Verification", error_message)
        else:
            QMessageBox.critical(self, "OTP Verification", "Unknown error")