import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget


class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Главная страница', self)
        layout.addWidget(label)

        button = QPushButton('Перейти на другую страницу', self)
        button.clicked.connect(self.go_to_other_page)
        layout.addWidget(button)

    def go_to_other_page(self):
        other_page = OtherPage()
        self.parent().setCentralWidget(other_page)


class OtherPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Другая страница', self)
        layout.addWidget(label)

        button = QPushButton('Вернуться на главную страницу', self)
        button.clicked.connect(self.go_to_main_page)
        layout.addWidget(button)

    def go_to_main_page(self):
        main_page = MainPage()
        self.parent().setCentralWidget(main_page)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Мое приложение')

        main_page = MainPage()
        self.setCentralWidget(main_page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())