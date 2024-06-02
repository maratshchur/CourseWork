import sys
import requests
from PySide6.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem

class TournamentApp(QTabWidget):
    def __init__(self, tournament_id):
        super().__init__()
        self.tournament_id = tournament_id
        self.setWindowTitle("Tournament Participation")
        self.resize(600, 400)
        self.load_tournament_data()

    def load_tournament_data(self):
        response = requests.get(f'http://127.0.0.1:8000/tournament/{self.tournament_id}/')
        data = response.json()
        self.setWindowTitle(data['title'])
        
        # Создаем вкладку для каждого раунда
        rounds = data['rounds']
        round_numbers = sorted(set([r['round_number'] for r in rounds]))
        
        for round_number in round_numbers:
            tab = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(QLabel(f"Words for Round {round_number}:"))
            for word in [r['word'] for r in rounds if r['round_number'] == round_number]:
                layout.addWidget(QLabel(word))
            tab.setLayout(layout)
            self.addTab(tab, f"Round {round_number}")
        
        # Вкладка для отображения других участников
        participants_tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Participants Results:"))
        
        participants_table = QTableWidget()
        participants_table.setRowCount(len(data['participants']))
        participants_table.setColumnCount(3)
        participants_table.setHorizontalHeaderLabels(["Username", "Place", "Score"])
        
        for row, participant in enumerate(data['participants']):
            participants_table.setItem(row, 0, QTableWidgetItem(participant['participant__user_id__username']))
            participants_table.setItem(row, 1, QTableWidgetItem(str(participant['place'])))
            participants_table.setItem(row, 2, QTableWidgetItem(str(participant['score'])))
        
        layout.addWidget(participants_table)
        participants_tab.setLayout(layout)
        self.addTab(participants_tab, "Participants")

def main():
    app = QApplication(sys.argv)
    tournament_id = 1  # Замените на нужный ID турнира
    demo = TournamentApp(tournament_id)
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()