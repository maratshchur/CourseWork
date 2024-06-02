import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QDialog, QLabel, QMessageBox, QLineEdit,\
    QListWidgetItem, QListWidget, QMenu, QListView
from PySide6.QtCore import QRect
from PySide6.QtGui import QAction
from functools import partial
from developers_info_page import DevelopersInfoPage
from email_verification import VerifyEmailPage
from faq_page import FAQDialog
from login import LoginPage
from profile_page import ProfilePage
from register import RegisterPage
from top_list import TopListPage
from urls import BASE_URL
import requests
from UI.ui_user_main_window import Ui_Dialog
from session import check_session, get_session_id
from PySide6.QtCore import Qt

class UserPage(QDialog):
    def __init__(self, response):
        super(UserPage, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.set_ui_connections(response)
                
                
    def set_ui_connections(self, response):   
        self.username = response.json().get('username')
        self.sorted_words_closeness = None 
        self.current_game = None
        self.attempts = None
        self.training_mode = False
        self.hints = None
        self.current_date = None
        self.current_word = None
        self.words_closeness = dict()
        self.word_guessed = None
                
        self.ui.profile_button.clicked.connect(self.show_my_profile_page)
        self.ui.top_list_button.clicked.connect(self.show_top_list_page)
        self.ui.login_button.clicked.connect(self.log_out)
        self.ui.input_field.returnPressed.connect(lambda: self.guess_word(f"{BASE_URL}/guess_word"))
        self.ui.hint_button.clicked.connect(lambda:  self.get_hint(f"{BASE_URL}/get_hint"))
        self.ui.other_games_button.clicked.connect(lambda: self.show_other_games(f"{BASE_URL}/words"))
        self.ui.else_button.clicked.connect(self.show_game_options)


        
        self.ui.other_games_button.setAutoDefault(False)
        self.ui.profile_button.setAutoDefault(False)
        self.ui.top_list_button.setAutoDefault(False)
        self.ui.login_button.setAutoDefault(False)
        self.ui.hint_button.setAutoDefault(False)


        

        self.ui.input_field.setPlaceholderText("Введите слово")

        self.get_daily_word(f"{BASE_URL}/daily_word")
        self.download_game_stats(f"{BASE_URL}/game/data")
        
    def show_developers_info_page(self):
        self.developers_info_page = DevelopersInfoPage()
        self.developers_info_page.exec()
        
    def show_faq_page(self):
        self.faq_page = FAQDialog()
        self.faq_page.exec()
        
    def show_my_profile_page(self):
    
        self.profile_page = ProfilePage(self.username)
        self.profile_page.exec()
                
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
        text = self.ui.input_field.text().strip().lower()
        if self.training_mode == True:
            self.guess_training_word(text)
        else:
            self.guess_rating_word(url, text)
    
    def guess_training_word(self, text):
        response = requests.get(f"{BASE_URL}/guess_training_word", params={'game_word': self.current_word, 'user_word': text})
        if response.status_code==200:
            if response.json().get("guessed"):
                
                self.word_guessed = True
                QMessageBox.information(self, "Победа", f"Вы угадали слово\n")
                closeness = response.json().get("closeness")
                self.add_word_to_list(text, closeness)
                return
            
            closeness = response.json().get("closeness")
            self.add_word_to_list(text, closeness)
            self.attempts+=1
        
    def guess_rating_word(self,url,text):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        response = requests.get(url, headers=headers, params={'game_word': self.current_word, 'user_word': text, 'game_number':self.current_game})
        
        if response.status_code==200:
            if response.json().get("guessed"):
                
                self.word_guessed = True
                rating = self.calculate_rating()
                QMessageBox.information(self, "Победа", f"Вы угадали слово\nВам начисляется {rating} рейтинга")
                self.give_rating_to_user(rating)
                self.inc_game_number()
                self.save_game_data()
                closeness = response.json().get("closeness")
                self.add_word_to_list(text, closeness)
                return
            
            closeness = response.json().get("closeness")
            self.add_word_to_list(text, closeness)
            
            if not response.json().get("guessed_earlier"):
                self.attempts+=1
                
    def calculate_rating(self):
        rating = 100 - self.hints*10
        if rating<0:
            rating = 0
        return rating
    
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
            response = requests.get(url, params = {'most_close_word_number': self.sorted_words_closeness[0][0], 'current_word': self.current_word})
        else:
            response = requests.get(url, params = {'most_close_word_number': 500, 'current_word': self.current_word})
            
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
                
        train_action = QAction("Тренировка", self)
        train_action.triggered.connect(self.training_chosen)
        menu.addAction(train_action)   
        menu.exec(self.ui.other_games_button.mapToGlobal(self.ui.other_games_button.rect().center()))
           
    def training_chosen(self):
        self.training_mode = True
        self.save_game_data()
        self.hide_rating_game_labels()
        self.clear_game_stats()
        self.update_ui()
        self.current_word = requests.get(f"{BASE_URL}/training_word").json().get("word")
        print(self.current_word)
        # Еще добавить кнопку сдаться

    
    def clear_game_stats(self):
        self.attempts = 0
        self.sorted_words_closeness = []
        self.current_game = None
        self.hints = 0
        self.current_date = None
        self.current_word = None
        self.words_closeness = dict()
        self.word_guessed = None
        
    def hide_rating_game_labels(self):
        # self.ui.attempts_label.hide()
        self.ui.current_word_list.clear()
        self.ui.game_number_label.hide()
        # self.ui.hints_label.hide()
        self.ui.date_label.hide()
        
        
    # Переделать !!!!
    def game_chosen(self, _,current_game, current_date, current_word):
        if not self.training_mode:
            self.save_game_data()
        else:
            self.training_mode = False
            self.show_labels()
        self.word_guessed = False
        self.current_game = _
        self.current_date = current_game
        self.current_word = current_date

        self.download_game_stats(f"{BASE_URL}/game/data")
        
    def show_labels(self):
        self.ui.game_number_label.show()
        self.ui.date_label.show()
    
    def show_game_options(self):
        menu = QMenu(self)

        if self.training_mode:         
            give_up_action = QAction("Сдаться", self)
            give_up_action.triggered.connect(self.give_up)
            menu.addAction(give_up_action) 
              
        faq_action = QAction("FAQ", self)
        faq_action.triggered.connect(self.show_faq_page)
        menu.addAction(faq_action)
        
        developers_action = QAction("О разработчиках", self)
        developers_action.triggered.connect(self.show_developers_info_page)
        menu.addAction(developers_action)
        
        menu.exec(self.ui.else_button.mapToGlobal(self.ui.else_button.rect().center()))
        
    def give_up(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Game Over")
        msg_box.setText(f"""
    <div style="text-align: center; font-family: Arial, sans-serif; color: #333;">
        <p style="font-size: 18px;">Было загадано слово</p>
        <p style="font-size: 24px; color: #2E86C1; font-weight: bold;">
            <font size="5">{self.current_word.upper()}</font>
        </p>
    </div>
""")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setIcon(QMessageBox.NoIcon)  # Устанавливаем иконку в NoIcon
        msg_box.exec_()
        self.add_word_to_list(self.current_word, 1)
        
    def update_ui(self):
        self.ui.input_field.clear()
        self.ui.current_word_list.clear()
        self.ui.attempts_label.setText(f"Попытки: {self.attempts}")
        self.ui.hints_label.setText(f"Подсказки: {self.hints}")
        self.ui.game_number_label.setText(f"Игра № {self.current_game}")
        self.ui.date_label.setText(f"От: {self.current_date}")
        
        for key, value in self.sorted_words_closeness:
                self.ui.current_word_list.addItem(QListWidgetItem(f"{key}. {value}"))

            
    def add_word_to_list(self, word, closeness):
        self.words_closeness[closeness] = word
        self.sorted_words_closeness = sorted(self.words_closeness.items())
        self.update_ui()
            

    def log_out(self):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        self.save_game_data()
        response = requests.post(f"{BASE_URL}/logout", headers=headers)
        if response.status_code == 200:
            QMessageBox.information(self, "Logged out", "You have been logged out successfully!")
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Failed to log out. Please try again.")
    
    def show_top_list_page(self):
        self.top_list_page = TopListPage()
        self.top_list_page.exec()
    
    def save_game_data(self):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        response = requests.put(f"{BASE_URL}/save_statistic", headers=headers, json={
    'game_number': self.current_game,
    'attempts': self.attempts,
    'hints': self.hints,
    'words': self.words_closeness,
    'guessed': self.word_guessed})

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserPage()
    window.show()
    sys.exit(app.exec())