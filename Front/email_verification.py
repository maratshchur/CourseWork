from PySide6.QtWidgets import QApplication, QDialog, QLineEdit,  QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtCore import QSettings
import sys
import requests
import json
from urls import BASE_URL
from UI.ui_email_verification_dialog import Ui_Dialog

class VerifyEmailPage(QDialog, Ui_Dialog):
    def __init__(self, email, username):
        super(VerifyEmailPage, self).__init__()
        self.setupUi(self)
        self.email = email
        self.username = username
        
        self.first_digit_input.textChanged.connect(self.focus_next_field)
        self.second_digit_input.textChanged.connect(self.focus_next_field)
        self.third_digit_input.textChanged.connect(self.focus_next_field)
        self.fourth_digit_input.textChanged.connect(self.focus_next_field)
        self.fifth_digit_input.textChanged.connect(self.focus_next_field)
        self.sixth_digit_input.textChanged.connect(self.submit_button.setFocus)
        
        self.resend_otp_button.clicked.connect(lambda: self.resend_otp(email))
        self.submit_button.clicked.connect(self.verify_otp)
        
        self.instructions_text.setText(f"Мы отправили код подтверждения на почту<br><b>{email}</b>")
        
    def resend_otp(self, email):
        response = requests.post(f'{BASE_URL}/resend-otp', data={'otp_email': email})

        if response.status_code==200:
            QMessageBox.information(self, 'Succes',response.json().get('message', 'New OTP send'))
        else:
            error_message = response.json().get('error', 'Unknown error')
            QMessageBox.critical(self, "OTP Resent Error", error_message)

    def verify_otp(self):
        from login import LoginPage
        otp = self.get_otp_code()
        if otp is None:
            QMessageBox.critical(self, "Подтверждение почты", "Пожалуйста заполните все поля")
            return
        response = requests.post(f'{BASE_URL}/verify-email/{self.username}', data={'otp_code': otp})
        if response.status_code == 200:
            QMessageBox.information(self, "OTP Verification", response.json().get('message', 'Successfully verificated'))
            self.done(QDialog.Accepted)
            # self.close()
        elif response.status_code == 401:
            error_message = response.json().get('error', 'Invalid OTP')
            QMessageBox.critical(self, "OTP Verification", error_message)
        else:
            QMessageBox.critical(self, "OTP Verification", "Unknown error")
            
    def get_otp_code(self):
        otp_code = ""
        if self.first_digit_input.text()!= "":
            otp_code += self.first_digit_input.text()
        else:
            return None
        if self.second_digit_input.text()!= "":
            otp_code += self.second_digit_input.text()
        else:
            return None
        if self.third_digit_input.text()!= "":
            otp_code += self.third_digit_input.text()
        else:
            return None
        if self.fourth_digit_input.text()!= "":
            otp_code += self.fourth_digit_input.text()
        else:
            return None
        if self.fifth_digit_input.text()!= "":
            otp_code += self.fifth_digit_input.text()
        else:
            return None
        if self.sixth_digit_input.text()!= "":
            otp_code += self.sixth_digit_input.text()
        else:
            return None
        return otp_code
        
        
        
    def focus_next_field(self):
        sender = self.sender()
        if sender == self.first_digit_input:
            self.second_digit_input.setFocus()
        elif sender == self.second_digit_input:
            self.third_digit_input.setFocus()
        elif sender == self.third_digit_input:
            self.fourth_digit_input.setFocus()
        elif sender == self.fourth_digit_input:
            self.fifth_digit_input.setFocus()
        elif sender == self.fifth_digit_input:
            self.sixth_digit_input.setFocus()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = VerifyEmailPage('joesl', 'ersfd')
    dialog.show()
    sys.exit(app.exec())