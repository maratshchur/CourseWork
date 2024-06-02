from PySide6.QtWidgets import QApplication, QDialog, QLineEdit,  QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox\
    ,QListWidgetItem
import sys
import requests
import json
from email_verification import VerifyEmailPage
from profile_page import ProfilePage
from urls import BASE_URL
from UI.ui_top_list_dialog import Ui_Dialog

class TopListPage(QDialog, Ui_Dialog):
    def __init__(self):
        super(TopListPage, self).__init__()
        self.setupUi(self)
        response = requests.get(f"{BASE_URL}/top_list")
        if response.status_code == 200:
            self.top_users = response.json()
            self.top_list.clear()
            a = 0
            for user in self.top_users['top_users']:
                a+=1
                self.top_list.addItem(QListWidgetItem(f"{a}. {user['username']}"))
        self.top_list.itemClicked.connect(self.render_profile)
        
        
        
    def render_profile(self, item):
        username = item.text().split('.')[1].strip()  # Get the username from the item text
        self.profile_page = ProfilePage(username)
        self.profile_page.exec()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = TopListPage()
    dialog.show()
    sys.exit(app.exec())