from PySide6.QtWidgets import QApplication, QDialog, QLineEdit,  QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
import sys
import requests
import json
from email_verification import VerifyEmailPage
from urls import BASE_URL
from UI.ui_profile_dialog import Ui_Dialog

class ProfilePage(QDialog, Ui_Dialog):
    def __init__(self, username):
        super(ProfilePage, self).__init__()
        self.setupUi(self)
        self.username = username
        self.rating, self.games_played = self.get_profile_data(f"{BASE_URL}/profile")
        
        self.username_label.setText(f"Имя пользователя: {self.username}")  
        self.username_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")

        self.rating_label.setText(f"Рейтинг: {str(self.rating)}")
        self.rating_label.setStyleSheet("font-size: 14px; color: #666; font-weight: bold")

        self.games_played_label.setText(f"Игр сыграно: {str(self.games_played)}")
        self.games_played_label.setStyleSheet("font-size: 14px; color: #666; font-weight: bold")

        self.setStyleSheet("""
            background-color: #F4EDE2; 
        """)

    def get_profile_data(self, url):
        response = requests.get(url, {"username": self.username})
        rating = response.json().get('rating')
        games_played = response.json().get('games_played')
        return rating, games_played

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = ProfilePage('marat')
    dialog.show()
    sys.exit(app.exec())