from PySide6.QtWidgets import QApplication, QDialog, QLineEdit,  QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
import sys
import requests
import json
from email_verification import VerifyEmailPage
from urls import BASE_URL
from UI.ui_developers_info_dialog import Ui_Dialog

class DevelopersInfoPage(QDialog, Ui_Dialog):
    def __init__(self):
        super(DevelopersInfoPage, self).__init__()
        self.setupUi(self)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = DevelopersInfoPage()
    dialog.show()
    sys.exit(app.exec())