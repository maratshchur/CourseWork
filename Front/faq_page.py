import sys
from PySide6.QtWidgets import QApplication, QHBoxLayout, QListWidget, QListWidgetItem, QPushButton, QTextEdit,\
    QVBoxLayout, QWidget, QDialog
from PySide6.QtCore import QSize
import requests
from urls import BASE_URL

class FAQItem(QListWidgetItem):
    def __init__(self, question, answer):
        super().__init__()
        self.question = question
        self.answer = answer
        self.button = QPushButton("More")
        self.button.clicked.connect(self.toggleAnswer)
        self.answer_widget = None
        self.setSizeHint(QSize(200, 50))  # adjust the size hint for initial display

    def toggleAnswer(self):
        if self.answer_widget:
            self.answer_widget.deleteLater()
            self.answer_widget = None
            self.button.setText("More")
            self.setSizeHint(QSize(200, 50))  # reset the size hint
        else:
            self.answer_widget = self.createAnswerWidget()
            self.listWidget().setItemWidget(self, self.answer_widget)
            self.button.setText("Less")
            self.setSizeHint(QSize(200, 150))  # adjust the size hint for expanded display

    def createAnswerWidget(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setText(self.answer)
        text_edit.setStyleSheet("QTextEdit { background-color: #f0f0f0; border: none; }")
        layout.addWidget(text_edit)
        return widget

class FAQList(QListWidget):
    def __init__(self):
        super().__init__()
        self.loadFAQs()
        
    def loadFAQs(self):
        url = f'{BASE_URL}/faq'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data["answers"]:
                question = item["question"]
                answer = item["answer"]
                self.addFAQItem(question, answer)
        else:
            print("Error:", response.status_code)

    def addFAQItem(self, question, answer):
        item = FAQItem(question, answer)
        widget = QWidget()
        layout = QHBoxLayout()
        text_edit = QTextEdit(question)
        text_edit.setReadOnly(True)
        text_edit.setStyleSheet("QTextEdit { background-color: #ffffff; border: 1px solid #cccccc; }")
        layout.addWidget(text_edit)
        layout.addWidget(item.button)
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)
        self.addItem(item)
        self.setItemWidget(item, widget)

class FAQDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.faq_list = FAQList()
        layout = QVBoxLayout()
        layout.addWidget(self.faq_list)
        self.setLayout(layout)

        # Set the window size
        self.resize(800, 600)  # Change the size as needed

        # Add main window stylesheet
        self.setStyleSheet("""
            QWidget {
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QListWidget {
                background-color: #f5f5f5;
                border: 1px solid #cccccc;
            }
            QPushButton {
                background-color: #808080; 
                color: white;
                border: none;
                padding: 5px 10px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 14px;
                margin: 2px 1px;
                cursor: pointer;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FAQDialog()
    window.show()
    sys.exit(app.exec())