from PySide6.QtWidgets import QApplication, QDialog, QLineEdit,  QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QMainWindow
from PySide6.QtCore import QSettings
import sys
import requests
import json
from email_verification import VerifyEmailPage
from urls import BASE_URL
from UI.ui_login_dialog import Ui_Dialog
from register import RegisterPage
from UI.ui_main_window import Ui_MainWindow  # Import the UI for MainWindow

class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.login_button.clicked.connect(self.login)

    def login(self):
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()

        response = requests.post(f'{BASE_URL}/login', data={'username': username, 'password': password})

        if response.status_code == 200:
            self.session_id = response.json()['session_id']
            # Store the session ID securely
            settings = QSettings('MyCompany', 'MyApp')
            settings.setValue('session_id', self.session_id)
            
            self.accept()
            self.done(QDialog.Accepted)
            self.close()

            # Create and show the MainWindow
            

        else:
            QMessageBox.critical(self, 'Error', response.json().get('error', 'Unknown error'))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Initialize your main window UI here


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = LoginPage()
    dialog.show()
    sys.exit(app.exec())