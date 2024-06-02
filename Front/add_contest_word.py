import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QMessageBox
from PySide6.QtGui import QMovie
from PySide6.QtCore import QUrl, Slot, QByteArray
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from email_verification import VerifyEmailPage
from session import get_session_id
from urls import BASE_URL
from UI.ui_add_word_dialog import Ui_Dialog
from register import RegisterPage

class AddWordPage(QDialog):
    def __init__(self):
        super(AddWordPage, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lineEdit.returnPressed.connect(self.add_word)
        self.ui.lineEdit.setPlaceholderText("Введите слово")
        
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.on_reply_finished)
        
        self.loading_indicator = QLabel(self)
        self.loading_indicator.resize(40, 40)
        self.loading_indicator.move(160, 70)  # Adjust the position as needed
        self.loading_movie = QMovie("D:/4_SEM/CourseWork/Front/images/ZKZg.gif")
        self.loading_indicator.setMovie(self.loading_movie)
        self.loading_indicator.setScaledContents(True)
        self.loading_indicator.hide()

    @Slot()
    def add_word(self):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        word = self.ui.lineEdit.text().strip().lower()
        if not word:
            QMessageBox.critical(self, "Ошибка", "Введите слово")
            return
        
        # Hide the input line edit and show the loading indicator
        self.ui.lineEdit.hide()
        self.loading_indicator.show()
        self.loading_movie.start()

        url = QUrl(f"{BASE_URL}/download_word_files")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/x-www-form-urlencoded")
        
        # Set custom headers
        for key, value in headers.items():
            request.setRawHeader(key.encode('utf-8'), value.encode('utf-8'))
        
        # Convert the data to application/x-www-form-urlencoded format
        data = QByteArray(f'word={word}'.encode('utf-8'))

        self.network_manager.post(request, data)

    @Slot(QNetworkReply)
    def on_reply_finished(self, reply):
        self.loading_movie.stop()
        self.loading_indicator.hide()
        self.ui.lineEdit.show()

        if reply.error() == QNetworkReply.NoError:
            response_data = reply.readAll().data()
            # Process the response data if needed
            QMessageBox.information(self, "", "Слово добавлено успешно")
            self.close()
        else:
            QMessageBox.critical(self, "Ошибка", "Слова не существует")

        reply.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = AddWordPage()
    dialog.show()
    sys.exit(app.exec())