from functools import partial
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDialog, QLabel, QMainWindow, QMessageBox, QLineEdit,\
    QListWidgetItem, QListWidget, QMenu
from PyQt6.QtGui import QAction
from login import LoginPage
from profile_page import ProfilePage
from register import RegisterPage
import sys
from urls import BASE_URL
import requests
from session import check_session, get_session_id

class MainPage(QMainWindow):
    def __init__(self):
        response = check_session(f"{BASE_URL}/check_session")
        if  response.status_code==200:
            super().__init__()
            self.username = response.json().get('username')
            self.sorted_words_closeness = None 
            self.current_game = None
            self.attempts = None
            self.hints = None
            self.current_date = None
            self.current_word = None
            self.words_closeness = dict()
            self.word_guessed = None
            
            self.current_word_list = QListWidget()
            self.game_number_label = QLabel("Игра №:")
            self.attempts_label = QLabel("")
            self.hints_label = QLabel("")
            self.date_label = QLabel("Дата:")
            self.input_field = QLineEdit()
            self.login_button = QPushButton("Войти")
            self.hint_button = QPushButton("Подсказка")
            self.other_games_button = QPushButton("Другие игры")
            self.profile_button = QPushButton("Профиль")
            self.profile_button.clicked.connect(self.show_my_profile_page)

            self.login_button.clicked.connect(self.show_login_page)
            self.input_field.returnPressed.connect(lambda: self.guess_word(f"{BASE_URL}/guess_word"))
            self.hint_button.clicked.connect(lambda:  self.get_hint(f"{BASE_URL}/get_hint"))
            self.other_games_button.clicked.connect(lambda: self.show_other_games(f"{BASE_URL}/words"))

            central_widget = QWidget()
            self.setCentralWidget(central_widget)

            layout = QVBoxLayout()
            layout.addWidget(self.profile_button)
            layout.addWidget(self.input_field)
            layout.addWidget(self.login_button)
            layout.addWidget(self.hint_button)
            layout.addWidget(self.other_games_button)

            layout.addWidget(self.game_number_label)
            layout.addWidget(self.date_label)
            layout.addWidget(self.current_word_list)
            layout.addWidget(self.attempts_label)
            layout.addWidget(self.hints_label)
            


            central_widget.setLayout(layout)
            self.setWindowTitle("Main Page")
            self.resize(400, 200)
            
            self.get_daily_word(f"{BASE_URL}/daily_word")
            self.download_game_stats(f"{BASE_URL}/game/data")
        else:
            self.show_login_page()

    def show_my_profile_page(self):
    
        self.profile_page = ProfilePage(self.username)
        self.profile_page.show()
                
    def get_daily_word(self, url):
        response = requests.get(url)
        if response.status_code==200:
            response = response.json()
            self.current_word = response.get("word")
            self.current_game = response.get("game_number")
            self.current_date = response.get("date")
            
 
    

    def download_game_stats(self, url):
        self.words_closeness.clear()
        
        if self.current_game:
            session_id = get_session_id()
            headers = {'Cookie': f'sessionid={session_id}'}
            response = requests.get(url, headers=headers, params={'game_number': self.current_game})
            
            if response.status_code==200:
                response = response.json()
                
                if not response:
                    self.attempts = 0
                    self.hints = 0
                    self.sorted_words_closeness = sorted(self.words_closeness.items())
                    self.word_guessed = False 
                                   
                else:
                    self.attempts = response[0]['attempts']
                    self.hints = response[0]['hints']
                    self.word_guessed = response[0]['guessed']
                    
                    for key, value in response[0]['entered_words'].items():
                        self.words_closeness[int(key)]=value
                    self.sorted_words_closeness = sorted(self.words_closeness.items())                
                
                self.update_ui()    
        
    
    def guess_word(self, url):
        text = self.input_field.text().strip().lower()
        
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        response = requests.get(url, headers=headers, params={'game_word': self.current_word, 'user_word': text, 'game_number':self.current_game})
        
        if response.status_code==200:
            if response.json().get("guessed"):
                QMessageBox.information(self, "Победа", "Вы угадали слово!!!")
                self.word_guessed = True
                self.give_rating_to_user(100)
                self.inc_game_number()
                self.save_game_data()
                closeness = response.json().get("closeness")
                self.add_word_to_list(text, closeness)
                return
            
            closeness = response.json().get("closeness")
            self.add_word_to_list(text, closeness)
            
            if not response.json().get("guessed_earlier"):
                self.attempts+=1
            
    def give_rating_to_user(self, quantity):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        response = requests.put(f"{BASE_URL}/add_rating", headers=headers, params={'rating_quantity': quantity})

    def inc_game_number(self):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        response = requests.put(f"{BASE_URL}/add_games_quantity", headers=headers)
        
        
    def get_hint(self,url):
        
        if self.sorted_words_closeness:
            response = requests.get(url, params = {'most_close_word_number': self.sorted_words_closeness[0][0], 'game_number': self.current_game})
        else:
            response = requests.get(url, params = {'most_close_word_number': 500, 'game_number': self.current_game})
            
        if response.status_code==200:
            self.hints+=1
            closeness = response.json().get("closeness")
            word = response.json().get("word")
            self.add_word_to_list(word, closeness)
        
        
    def show_other_games(self, url):
        menu = QMenu(self)
        
        response = requests.get(url)
        
        if response.status_code==200:
            for word in response.json().get('data'):
                current_date = word.get("date")
                current_game = word.get("game_number")
                current_word = word.get("word")
                menu.addAction(QAction(f"Игра №{current_game} от {current_date}", self,\
                                       triggered=partial(self.game_chosen, current_game, current_date, current_word)))
                
        menu.exec(self.other_games_button.mapToGlobal(self.other_games_button.rect().center()))
        

    def game_chosen(self, current_game, current_date, current_word):
        self.save_game_data()
        self.word_guessed = False
        self.current_game = current_game
        self.current_date = current_date
        self.current_word = current_word

        self.download_game_stats(f"{BASE_URL}/game/data")
            
    def update_ui(self):
        self.input_field.clear()
        self.current_word_list.clear()
        self.attempts_label.setText(f"Попытки: {self.attempts}")
        self.hints_label.setText(f"Подсказки: {self.hints}")
        self.game_number_label.setText(f"Игра № {self.current_game}")
        self.date_label.setText(f"От: {self.current_date}")
        
        for key, value in self.sorted_words_closeness:
                self.current_word_list.addItem(QListWidgetItem(f"{key}. {value}"))
                
    
    def add_word_to_list(self, word, closeness):
        self.words_closeness[closeness] = word
        self.sorted_words_closeness = sorted(self.words_closeness.items())
        self.update_ui()
            
    
        

    def show_login_page(self):
        self.login_page = LoginPage()
        self.login_page.register_button.clicked.connect(self.show_register_page)
        self.login_page.register_button.clicked.connect(self.login_page.close)
        self.login_page.show()

    def show_register_page(self):
        self.register_page = RegisterPage()
        self.register_page.show()
        
        
    def closeEvent(self, event):
        self.save_game_data()
    
    
    def save_game_data(self):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        response = requests.put(f"{BASE_URL}/save_statistic", headers=headers, json={
    'game_number': self.current_game,
    'attempts': self.attempts,
    'hints': self.hints,
    'words': self.words_closeness,
    'guessed': self.word_guessed})



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_page = MainPage()
    main_page.show()
    sys.exit(app.exec())
    
    
