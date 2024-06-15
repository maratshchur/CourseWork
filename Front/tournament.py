import datetime
from PySide6.QtWidgets import QDialog, QVBoxLayout, QWidget, QTabWidget, QApplication, QListWidgetItem, QMessageBox, QLabel
from PySide6.QtGui import QColor, QPalette, QBrush, QColor
from PySide6.QtCore import QEvent, QTimer

import sys
import requests
from session import get_session_id
from urls import BASE_URL
from UI.tornament_tab_widget import Ui_Dialog
from UI.form import TournamentForm

class TournamentPage(QDialog):
    def __init__(self, tournament_id):
        super(TournamentPage, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.session_id = get_session_id()

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.get_rankings)
        self.timer1.start(3000)  # 3 seconds in milliseconds

        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.update_remaining_time)
        self.timer2.start(1000)  # 1 second in milliseconds

        self.ui.tabWidget.setTabPosition(QTabWidget.West)
        self.tournament_id = tournament_id

        self.init_variables()
        self.get_tournament_data()
        self.update_remaining_time()
        self.make_tabs()
        self.ui.tabWidget.currentChanged.connect(self.on_tab_changed)
        self.download_game_stats(self.current_round)

    def init_variables(self):
        self.tournament_words = []
        self.rounds = 0
        self.title = None
        self.words_closeness = {}
        self.sorted_words_closeness = []
        self.current_round = 1
        self.word_id = None
        self.current_word = None
        self.word_guessed = False
        self.guessed_rounds = set()

    def get_tournament_data(self):
        response = requests.get(f"{BASE_URL}/tournament/{self.tournament_id}/data/")
        if response.status_code == 200:
            data = response.json()
            self.title = data.get("title")
            self.tournament_words = [(word.get("word"), word.get("round_number"), word.get("word_id")) for word in data.get("words", [])]
            self.tournament_end = datetime.datetime.strptime(data.get("end"), "%Y-%m-%dT%H:%M:%SZ")
            self.tournament_start = datetime.datetime.strptime(data.get("end"), "%Y-%m-%dT%H:%M:%SZ")

        self.get_rankings()

    def update_remaining_time(self):
        remaining_time = self.tournament_end - datetime.datetime.now()
        if remaining_time.total_seconds() > 0:
            hours, remainder = divmod(remaining_time.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            self.ui.remaining_time_label.setText(f"Окончание через {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")
        else:
            self.ui.remaining_time_label.setText("Турнир закончился")
            self.show_tournament_ended_notification()

    def show_tournament_ended_notification(self):
        QMessageBox.information(self, "Турнир", "Время вышло. Турнир окончен")
        self.close()  # Close the dialog when the tournament has ended

    def get_rankings(self):
        response = requests.get(f"{BASE_URL}/tournament/{self.tournament_id}/stats")  # Make a request to the server
        data = response.json()  # Assume the server returns the data in JSON format
        self.ui.standings_list.clear()

        for item in data:
            participant, words_guessed = item  # Unpack the tuple
            item_text = f"{participant}: {words_guessed} угадано"
            self.ui.standings_list.addItem(QListWidgetItem(item_text))

    def make_tabs(self):
        self.tabs = []
        self.forms = []
        for i in range(len(self.tournament_words)):
            tab = QWidget()
            tab_layout = QVBoxLayout()
            form_ui = TournamentForm()
            form_ui.ui.input_field.returnPressed.connect(lambda checked=False, url=f"{BASE_URL}/tournament/guess_word/": self.guess_word(url))
            tab_layout.addWidget(form_ui)
            tab.setLayout(tab_layout)
            self.ui.tabWidget.addTab(tab, f"Раунд {i + 1}")
            self.tabs.append(tab)
            self.forms.append(form_ui)

    def on_tab_changed(self, index):
        self.save_game_data()
        self.current_round = index + 1
        self.download_game_stats(self.current_round)

    def download_game_stats(self, round):
        self.words_closeness.clear()
        self.word_id = self.get_word_id_by_round(round)
        self.current_word = self.get_word_by_round(round)

        if self.word_id:
            headers = {'Cookie': f'sessionid={self.session_id}'}
            response = requests.get(f"{BASE_URL}/tournaments/{self.tournament_id}/statistic/", headers=headers)
            if response.status_code == 200:
                data = response.json()
                if not data:
                    self.attempts = 0
                    self.word_guessed = False
                else:
                    for stat in data:
                        if stat.get('guessed'):
                            self.guessed_rounds.add(stat.get("round_number"))
                        if self.current_round == stat.get("round_number"):
                            self.attempts = stat['attempts']
                            self.word_guessed = stat['guessed']
                            for key, value in stat['entered_words'].items():
                                self.words_closeness[int(key)] = value
                    self.sorted_words_closeness = sorted(self.words_closeness.items())
                self.update_ui(round)
                    
                    
    def update_ui(self, round):
        form_ui = self.forms[round - 1]
        form_ui.ui.input_field.clear()
        form_ui.ui.current_word_list.clear()
        form_ui.ui.label.setText(f"Попытки: {self.attempts}")
        self.ui.title_label.setText(f"{self.title}")
        for key, value in self.sorted_words_closeness:
            item = QListWidgetItem(f"{key}. {value}")
            if key == 1:
                item.setBackground(QBrush(QColor("skyblue")))  # Bright gold for the winning word!
            elif key < 300:
                item.setBackground(QBrush(QColor("palegreen")))  # Light green
            elif key < 1000:
                item.setBackground(QBrush(QColor("orange")))  # Light orange
            else:
                item.setBackground(QBrush(QColor("salmon")))  # Light red
            form_ui.ui.current_word_list.addItem(item)

    def get_word_id_by_round(self, round):
        for word in self.tournament_words:
            if word[1] == round:
                return word[2]
        return None

    def get_word_by_round(self, round):
        for word in self.tournament_words:
            if word[1] == round:
                return word[0]
        return None

    def guess_word(self, url):
        form_ui = self.forms[self.current_round - 1]
        text = form_ui.ui.input_field.text().strip().lower()
        headers = {'Cookie': f'sessionid={self.session_id}'}
        response = requests.get(url, headers=headers, params={'game_word': self.current_word, 'user_word': text, 'word_id': self.word_id})

        if response.status_code == 200:
            data = response.json()
            closeness = data.get("closeness")
            self.add_word_to_list(text, closeness)

            if data.get("guessed"):
                self.word_guessed = True
                self.guessed_rounds.add(self.current_round)
                self.save_game_data()
                if self.all_words_guessed():
                    pass
            else:
                self.attempts += 1
                
        self.update_ui(self.current_round)

    def all_words_guessed(self):
        if all(word[1] in self.guessed_rounds for word in self.tournament_words):
            headers = {'Cookie': f'sessionid={self.session_id}'}
            response = requests.get(f"{BASE_URL}/tournament/{self.tournament_id}/get_completion_time/", headers=headers)
            if response.status_code == 200:
                data = response.json()
                if not data.get('completion_time'):  # Check if completion time is already saved
                    completion_time = datetime.datetime.now()
                    response = requests.put(f"{BASE_URL}/tournament/{self.tournament_id}/save_completion_time/", headers=headers, json={
                        'completion_time': completion_time.isoformat()
                    })
                    if response.status_code == 200:
                        self.show_notification("Победа", "Вы угадали все слова\nВы узнаете результаты после окончания турнира\nВремя выполнения: {}".format(completion_time.strftime("%H:%M:%S")))
                    else:
                        self.show_notification("Ошибка", "Не удалось сохранить время выполнения")
                else:
                    self.show_notification("Победа", "Вы уже угадали все слова\nВы узнаете результаты после окончания турнира")
            return True
        return False

    def show_notification(self, title, message):
        QMessageBox.information(self, title, message)
        
    def add_word_to_list(self, word, closeness):
        self.words_closeness[closeness] = word
        self.sorted_words_closeness = sorted(self.words_closeness.items())
        self.update_ui(self.current_round)

    def closeEvent(self, event):
        self.timer1.stop()  # Stop the timer when the dialog is closed
        self.timer2.stop()
        self.save_game_data()
        super().closeEvent(event)

    def save_game_data(self):
        headers = {'Cookie': f'sessionid={self.session_id}'}
        response = requests.put(f"{BASE_URL}/tournaments/save_statistic/", headers=headers, json={
            'tournament_id': self.tournament_id,
            'round_number': self.current_round,
            'word': self.current_word,
            'attempts': self.attempts,
            'words': self.words_closeness,
            'guessed': self.word_guessed
        })
        if response.status_code != 200:
            QMessageBox.critical(self, "Error", "Failed to save game data")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TournamentPage(1)
    window.show()
    sys.exit(app.exec())