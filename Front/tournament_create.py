import json
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QSpinBox, QDateTimeEdit, QTimeEdit, \
    QListWidget, QPushButton, QListWidgetItem, QInputDialog, QLabel, QTextEdit, QMessageBox, QDialog
from PySide6.QtCore import Qt, QUrl, QDateTime
from PySide6.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply

from add_contest_word import AddWordPage
from session import get_session_id
from urls import BASE_URL

class TournamentCreationWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet(self.getStylesheet())
        self.reply = None  # Хранит ссылку на reply
        self.nam = QNetworkAccessManager()  # Создаем менеджер сети один раз
        self.number_of_words = 0

    def getStylesheet(self):
        return """
        TournamentCreationWidget {
            background-color: #f0f0f0;
            border: 1px solid #cccccc;
            border-radius: 8px;
            padding: 16px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        QLineEdit, QTextEdit, QDateTimeEdit, QSpinBox, QListWidget {
            border: 1px solid #cccccc;
            border-radius: 4px;
            padding: 8px;
            font-size: 16px;
            background-color: #ffffff;
        }
        QLabel {
            font-size: 16px;
            color: #333333;
            margin-bottom: 8px;
        }
        QPushButton {
            background-color: #4CAF50;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        QPushButton:hover {
            background-color: #45A049;
        }
        QPushButton:pressed {
            background-color: #388E3C;
        }
        QListWidget::item {
            padding: 8px;
            margin: 2px 0;
            border-radius: 4px;
        }
        QListWidget::item:nth-child(even) {
            background-color: #f9f9f9;
        }
        QListWidget::item:nth-child(odd) {
            background-color: #e9e9e9;
        }
        """

    def initUI(self):
        self.createWidgets()
        self.setLayout(self.createLayout())
        self.connectSignals()

    def createWidgets(self):
        # Создаем виджеты
        self.headerLabel = QLabel("Создание турнира")
        self.headerLabel.setStyleSheet("font-weight: bold; font-size: 18px;")

        self.titleLineEdit = QLineEdit()
        self.titleLineEdit.setPlaceholderText("Введите название турнира")

        self.descriptionTextEdit = QTextEdit()
        self.descriptionTextEdit.setPlaceholderText("Введите описание турнира")

        self.startDateTimeLabel = QLabel("Время начала:")
        self.startDateTimeEdit = QDateTimeEdit()
        self.startDateTimeEdit.setDateTime(QDateTime.currentDateTime())  # set default date and time

        self.durationTimeLabel = QLabel("Длительность (минуты):")
        self.durationTimeEdit = QSpinBox()
        self.durationTimeEdit.setMinimum(1)
        self.durationTimeEdit.setMaximum(60)  # 1440 minutes = 24 hours

        self.wordsListLabel = QLabel("Слова:")
        self.wordsListWidget = QListWidget()

        self.addWordButton = QPushButton("Добавить слово")
        self.createTournamentButton = QPushButton("Создать турнир")

    def createLayout(self):
        # Создаем и компонуем layout
        layout = QVBoxLayout()
        layout.addWidget(self.headerLabel)
        layout.addWidget(self.titleLineEdit)
        layout.addWidget(self.descriptionTextEdit)
        layout.addWidget(self.startDateTimeLabel)
        layout.addWidget(self.startDateTimeEdit)
        layout.addWidget(self.durationTimeLabel)
        layout.addWidget(self.durationTimeEdit)
        layout.addWidget(self.wordsListLabel)
        layout.addWidget(self.wordsListWidget)
        layout.addWidget(self.addWordButton)
        layout.addWidget(self.createTournamentButton)
        return layout

    def connectSignals(self):
        # Подключаем сигналы к слотам
        self.addWordButton.clicked.connect(self.addWord)
        self.createTournamentButton.clicked.connect(self.createTournament)

    def addWord(self):
        self.addWordDialog = AddWordPage()
        self.addWordDialog.exec()
        word = self.addWordDialog.ui.lineEdit.text().strip().lower()
        if self.wordsListWidget.count() < 10:
            item = QListWidgetItem(word)
            self.wordsListWidget.addItem(item)
            self.number_of_words += 1
        else:
            QMessageBox.warning(self, "Ошибка", "В турнир можно добавить не более 10 слов")

    def createTournament(self):
        # Проверяем, что все поля заполнены
        if not self.formIsValid():
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        # Создаем турнир
        data = self.collectData()
        request, payload = self.createRequest(data)
        self.sendRequest(request, payload)

    def formIsValid(self):
        # Проверяем, что все поля заполнены
        if not self.titleLineEdit.text().strip():
            return False
        if not self.descriptionTextEdit.toPlainText().strip():
            return False
        if self.wordsListWidget.count() == 0:
            return False
        return True

    def collectData(self):
        # Собираем данные с формы
        title = self.titleLineEdit.text().strip()
        description = self.descriptionTextEdit.toPlainText().strip()
        start_date_time = self.startDateTimeEdit.dateTime()
        duration = int(self.durationTimeEdit.text())
        words = {i+1: item.text() for i, item in enumerate(self.wordsListWidget.findItems("", Qt.MatchContains))}

        # Формируем данные для отправки
        return {
            "title": title,
            "description": description,
            "number_of_words": self.number_of_words,
            "start_date_time": start_date_time.toString(Qt.ISODate),
            "duration": {
                "minutes": duration
            },
            "words": words
        }

    def createRequest(self, data):
        # Создаем запрос
        url = f"{BASE_URL}/create_tournament"  # замените на ваш URL
        request = QNetworkRequest(QUrl(url))
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        request.setRawHeader(b'Cookie', headers['Cookie'].encode('utf-8'))

        return request, json.dumps(data).encode("utf-8")

    def sendRequest(self, request, payload):
        # Отправляем запрос
        self.reply = self.nam.post(request, payload)
        self.reply.finished.connect(self.handleResponse)

    def handleResponse(self):
        # Обрабатываем ответ сервера
        if self.reply.error() != QNetworkReply.NoError:
            print("Error:", self.reply.errorString())
        else:
            print("Tournament created successfully!")
            response = json.loads(self.reply.readAll().data().decode())
            print("Response data:", response)
            self.close()

        self.reply.deleteLater()  # Удаляем объект reply после завершения обработки
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TournamentCreationWidget()
    window.show()
    sys.exit(app.exec())