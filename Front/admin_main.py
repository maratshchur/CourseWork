import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QDialog, QLabel, QMessageBox, QLineEdit,\
    QListWidgetItem, QListWidget, QMenu, QListView
from PySide6.QtCore import QRect
from PySide6.QtGui import QAction
from functools import partial
from add_daily_word import AddWordPage
from email_verification import VerifyEmailPage
from login import LoginPage
from profile_page import ProfilePage
from register import RegisterPage
from top_list import TopListPage
from urls import BASE_URL
import requests
from UI.ui_admin_main_page import Ui_Dialog
from session import check_session, get_session_id

class AdminPage(QDialog):
    def __init__(self):
        super(AdminPage, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add_game_button.pressed.connect(self.add_word)
        self.ui.users_list.itemClicked.connect(self.render_profile)
        self.ui.login_button.clicked.connect(self.logout)
        self.users_list = []
        self.games_list = []
        self.download_admin_panel_data()
        
    def logout(self):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        response = requests.post(f"{BASE_URL}/logout", headers=headers)
        if response.status_code == 200:
            QMessageBox.information(self, "Logged out", "You have been logged out successfully!")
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Failed to log out. Please try again.")
            
    def render_profile(self, item):
        username = item.text().split('.')[1].strip()  # Get the username from the item text
        self.profile_page = ProfilePage(username)
        self.profile_page.exec()
        
    def get_users_list(self):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        response = requests.get(f"{BASE_URL}/users_list", headers=headers)
        
        if response.status_code == 200:
            self.users_list.clear()
            for user in response.json().get('users'):
                self.users_list.append(user['username'])
        else:
            QMessageBox.critical(self, "Error", "Failed to retrieve users list")
        
    def get_games_list(self):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        response = requests.get(f"{BASE_URL}/words", headers=headers)
        
        if response.status_code == 200:
            daily_words = response.json().get('data')
            self.games_list.clear()
            for word in daily_words:
                self.games_list.append((word['game_number'], word['word'] ,word['date']))
        else:
            QMessageBox.critical(self, "Error", "Failed to retrieve daily words")
      
    def add_word(self):
       self.add_word_dialog = AddWordPage()
       self.add_word_dialog.exec()
       self.download_admin_panel_data()

  
    def update_ui(self):
        self.ui.users_list.clear()
        self.ui.games_list.clear()
        a=0
        for user in self.users_list:
            a+=1
            self.ui.users_list.addItem(QListWidgetItem(f"{a}. {user}"))
        for game in self.games_list:
            self.ui.games_list.addItem(QListWidgetItem(f"Игра: {game[0]}\nСлово: {game[1]}\nДата: {game[2]}"))
                
    def download_admin_panel_data(self):
        self.get_users_list()
        self.get_games_list()
        self.update_ui()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminPage()
    window.show()
    sys.exit(app.exec())