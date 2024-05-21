from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication, QMessageBox
import requests
from session import get_session_id
from urls import BASE_URL

class ProfilePage(QDialog):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle("Профиль")
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.rating, self.games_played = self.get_profile_data(f"{BASE_URL}/profile")
        
        self.username_label = QLabel(f"Имя пользователя: {self.username}")
        layout.addWidget(self.username_label)

        self.rating_label = QLabel(f"Рейтинг: {str(self.rating)}")
        layout.addWidget(self.rating_label)

        self.games_played_label = QLabel(f"Игр сыграно: {str(self.games_played)}")
        layout.addWidget(self.games_played_label)

        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)
        
    def get_profile_data(self, url):
            response = requests.get(url, {"username": self.username})
            rating = response.json().get('rating')
            games_played = response.json().get('games_played')
            return rating, games_played
            
