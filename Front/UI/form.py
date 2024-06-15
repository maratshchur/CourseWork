from PySide6.QtWidgets import QApplication, QDialog, QLineEdit,  QLabel, QPushButton, QVBoxLayout, QWidget
from UI.tournament_form import Ui_Form

class TournamentForm(QWidget):
    def __init__(self):
        super(TournamentForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.input_field.setPlaceholderText("Введите слово")
