import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QTextBrowser, QListWidget, QListWidgetItem, QDialog
from PyQt6.QtCore import Qt
import requests
import datetime

from session import get_session_id
from urls import BASE_URL

class MessageDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        self.initUI(message)

    def initUI(self, message):
        self.setWindowTitle("Message")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        textBrowser = QTextBrowser()
        textBrowser.setReadOnly(True)
        textBrowser.setText(message)
        textBrowser.setStyleSheet("background-color: #F4EDE2; border: 1px solid #ccc; padding: 10px;")
        layout.addWidget(textBrowser)

class MessageWindow(QDialog):
    def __init__(self, messages):
        super().__init__()
        self.messages = self.sortMessagesByDate(messages)
        self.session_id = get_session_id()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("User Messages")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.listWidget = QListWidget()
        self.listWidget.setStyleSheet("""
            background-color: #F4EDE2; 
            border: 1px solid #ccc;
            font-size: 16px;  /* Adjust the font size here */
        """)
        layout.addWidget(self.listWidget)
        self.displayMessages(self.messages)
        self.listWidget.itemClicked.connect(self.onItemClicked)

    def sortMessagesByDate(self, messages):
        return sorted(messages, key=lambda x: datetime.datetime.fromisoformat(x['created_at']), reverse=True)

    def displayMessages(self, messages):
        self.listWidget.clear()
        for index, message in enumerate(messages):
            item = QListWidgetItem()

            text = message.get('title')
            item.setText(text)
            item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            
            # # Alternate row colors
            # if index % 2 == 0:
            #     item.setBackground(Qt.GlobalColor.gray)
            # else:
            #     item.setBackground(Qt.GlobalColor.gray)
            
            self.listWidget.addItem(item)

    def onItemClicked(self, item):
        title = item.text().strip()
        for message in self.messages:
            title_text = message.get('title')
            if title == title_text:
                created_at = message.get('created_at')
                dt = datetime.datetime.fromisoformat(created_at)
                formatted_date = dt.strftime('%d %B %Y, %H:%M')
                dialog = MessageDialog(f"{message.get('title')}\n\n{message.get('message')}\n\n{formatted_date}")
                self.markMessageAsRead(message.get('id'))
                dialog.exec()
                break

    def markMessageAsRead(self, message_id):
        # Send request to server to update message status
        url = f"{BASE_URL}/messages/{message_id}/read/"
        headers = {"Authorization": f"Bearer {self.session_id}"}
        
        response = requests.put(url, headers=headers)
        if response.status_code == 200:
            print("Message marked as read successfully")
        else:
            print("Error marking message as read")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    messages = [
        {"id": 1, "created_at": "2023-06-01T12:00:00.064839+00:00", "title": "Welcome", "message": "Welcome to the app!", "read": False},
        {"id": 2, "created_at": "2023-06-02T14:30:00.123456+00:00", "title": "Update", "message": "The app has been updated.", "read": True},
    ]

    window = MessageWindow(messages)
    window.show()
    sys.exit(app.exec())