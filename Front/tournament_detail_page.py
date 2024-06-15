import datetime
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QDialog, QLabel, QTextBrowser, QGridLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

import requests
from session import get_session_id
from tournament import TournamentPage
from urls import BASE_URL


class TournamentDetailWindow(QDialog):
    def __init__(self, tournament_id, parent=None):
        super(TournamentDetailWindow, self).__init__(parent)
        self.tournament_id = tournament_id
        self.session_id = get_session_id()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Tournament Details")
        self.resize(400, 600)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)

        # Set dark theme style
        self.setStyleSheet("""
            QDialog {
                background-color: #F4EDE2; 
                color: #333;
            }
            QLabel, QTextBrowser {
                color: #333;
            }
            QTextBrowser {
                background-color: #FFFBF5; 

                border: none;
                padding: 10px;
            }
            QPushButton {
                background-color: #4CAF50; 
                color: #ffffff; 
                border: none; 
                padding: 10px 20px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
        """)

        # Create a label to display the tournament title
        self.title_label = QLabel()
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Create a text browser to display the tournament description
        self.description_browser = QTextBrowser()
        self.description_browser.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.description_browser)

        # Create a grid layout to display other tournament details
        self.details_layout = QGridLayout()
        self.details_layout.setSpacing(10)

        self.number_of_words_label = QLabel()
        self.start_label = QLabel()
        self.duration_label = QLabel()
        self.end_label = QLabel()

        for label in [self.number_of_words_label, self.start_label, self.duration_label, self.end_label]:
            label.setFont(QFont("Arial", 12))

        self.details_layout.addWidget(QLabel("Количество слов:", font=QFont("Arial", 12)), 0, 0)
        self.details_layout.addWidget(self.number_of_words_label, 0, 1)
        self.details_layout.addWidget(QLabel("Начало:", font=QFont("Arial", 12)), 1, 0)
        self.details_layout.addWidget(self.start_label, 1, 1)
        self.details_layout.addWidget(QLabel("Длительность:", font=QFont("Arial", 12)), 2, 0)
        self.details_layout.addWidget(self.duration_label, 2, 1)
        self.details_layout.addWidget(QLabel("Окончание:", font=QFont("Arial", 12)), 3, 0)
        self.details_layout.addWidget(self.end_label, 3, 1)

        self.layout.addLayout(self.details_layout)

        # Add a spacer item for better spacing
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

        if not self.check_user_participation():
            self.participate_button = QPushButton("Участвовать в турнире")
            self.participate_button.setFont(QFont("Arial", 14, QFont.Bold))
            self.participate_button.setCursor(Qt.PointingHandCursor)
            self.layout.addWidget(self.participate_button, alignment=Qt.AlignCenter)
            self.participate_button.clicked.connect(self.participate_in_tournament)
        else:
            self.tournament_button = QPushButton("Продолжить")
            self.tournament_button.setFont(QFont("Arial", 14, QFont.Bold))
            self.tournament_button.setCursor(Qt.PointingHandCursor)
            self.tournament_button.setStyleSheet("background-color: #FFA500; color: black;")
            self.layout.addWidget(self.tournament_button, alignment=Qt.AlignCenter)        
            self.tournament_button.clicked.connect(self.open_tournament_page)

        self.setLayout(self.layout)
        
        # Fetch the tournament data from the Django database
        self.fetch_tournament_data()
    
    def participate_in_tournament(self):
        headers = {'Cookie': f'sessionid={self.session_id}'}
        response = requests.post(f"{BASE_URL}/tournament/{self.tournament_id}/participate/", headers=headers)
        if response.status_code == 201:
            print("Participation successful!")
            self.open_tournament_page()
        else:
            print(f"Error: {response.status_code}")
            
    def open_tournament_page(self):
        self.profile_page = TournamentPage(self.tournament_id)
        self.profile_page.exec()
        self.close()
        
    def check_user_participation(self):
        try:
            headers = {'Cookie': f'sessionid={self.session_id}'}
            response = requests.get(f"{BASE_URL}/tournament/{self.tournament_id}/participation/", headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            data = response.json()
            return data.get("has_statistic", False)  # Return False if key is not present
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return False
    
    def fetch_tournament_data(self):
        response = requests.get(f"{BASE_URL}/tournament/{self.tournament_id}/data/")
        if response.status_code == 200:
            data = response.json()
            title = data['title']
            description = data['description']
            number_of_words = data['number_of_words']
            start = data['start']
            duration = data['duration']
            end = data['end']
            
            start_dt = datetime.datetime.fromisoformat(start.removesuffix('Z'))
            end_dt = datetime.datetime.fromisoformat(end.removesuffix('Z'))

        # Format the datetime strings
            start_str = start_dt.strftime('%Y-%m-%d %H:%M:%S')
            end_str = end_dt.strftime('%Y-%m-%d %H:%M:%S')


            # Update the UI with the tournament data
            self.title_label.setText(title)
            self.description_browser.setText(description)
            self.number_of_words_label.setText(f"{number_of_words}")
            self.start_label.setText(f"{start_str}")
            self.duration_label.setText(f"{duration} мин.")
            self.end_label.setText(f"{end_str}")
        else:
            print(f"Error: {response.status_code}")