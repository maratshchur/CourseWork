# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_user_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(684, 596)
        Dialog.setStyleSheet(u"QDialog{\n"
"background-color: #FFFBF5; /* \u0431\u0435\u043b\u044b\u0439 \u0431\u044d\u043a\u0433\u0440\u0430\u0443\u043d\u0434 */\n"
"}\n"
"QLabel {\n"
"    font-size: 14px; /* size of label text */\n"
"    font-weight: bold; /* bold label text */\n"
"}\n"
"QLineEdit {\n"
"    border: 1px solid #ccc; /* light gray border for input fields */\n"
"    border-radius: 5px; /* rounded corners for input fields */\n"
"    padding: 5px; /* padding for input fields */\n"
"	color: #423232;\n"
"    background-color: #FFFEFE; /* \u0431\u0435\u043b\u044b\u0439 \u0431\u044d\u043a\u0433\u0440\u0430\u0443\u043d\u0434 */\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none; /* no border for buttons */\n"
"    border-radius: 5px; /* rounded corners for buttons */\n"
"    padding: 10px 20px; /* padding for buttons */\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0; /* light gray background on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d0d0d0; /* dark gray background "
                        "on press */\n"
"}\n"
"")
        self.current_word_list = QListWidget(Dialog)
        self.current_word_list.setObjectName(u"current_word_list")
        self.current_word_list.setGeometry(QRect(20, 220, 391, 281))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.current_word_list.setFont(font)
        self.current_word_list.setStyleSheet(u"QListWidget {\n"
"    /* \u043e\u0431\u0449\u0438\u0439 \u0441\u0442\u0438\u043b\u044c \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: #F4EDE2;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"    background-color: #E6DAC3;\n"
"    border-bottom: 2px solid #aaa;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c"
                        "\u0435\u043d\u0442\u0430 */\n"
"    background-color: #C9C4B5;\n"
"    border-bottom: 2px solid #666;\n"
"    color: #333;\n"
"}\n"
"\n"
"QListWidget::item:selected:hover {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"    background-color: #B3A892;\n"
"    border-bottom: 2px solid #444;\n"
"    color: #222;\n"
"}\n"
"")
        self.login_button = QPushButton(Dialog)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(21, 31, 52, 48))
        icon = QIcon()
        icon.addFile(u"D:\\4_SEM\\CourseWork\\Front\\images\\67346.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setIconSize(QSize(40, 40))
        self.login_button.setFlat(True)
        self.profile_button = QPushButton(Dialog)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setGeometry(QRect(560, 20, 71, 65))
        icon1 = QIcon()
        icon1.addFile(u"D:\\4_SEM\\CourseWork\\Front\\images\\download1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_button.setIcon(icon1)
        self.profile_button.setIconSize(QSize(45, 45))
        self.profile_button.setFlat(True)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 30, 151, 51))
        font1 = QFont()
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"   color: #423232;\n"
"    font-size: 26px; /* size of label text */\n"
"    font-weight: bold; /* bold label text */\n"
"background-color: #FFFBF5; /* \u0431\u0435\u043b\u044b\u0439 \u0431\u044d\u043a\u0433\u0440\u0430\u0443\u043d\u0434 */\n"
"\n"
"}\n"
"")
        self.hint_button = QPushButton(Dialog)
        self.hint_button.setObjectName(u"hint_button")
        self.hint_button.setGeometry(QRect(580, 520, 75, 71))
        icon2 = QIcon()
        icon2.addFile(u"D:\\4_SEM\\CourseWork\\Front\\images\\png-clipart-computer-icons-idea-brainstorming-others-miscellaneous-image-file-formats.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hint_button.setIcon(icon2)
        self.hint_button.setIconSize(QSize(50, 50))
        self.hint_button.setFlat(True)
        self.top_list_button = QPushButton(Dialog)
        self.top_list_button.setObjectName(u"top_list_button")
        self.top_list_button.setGeometry(QRect(500, 30, 61, 51))
        icon3 = QIcon()
        icon3.addFile(u"D:\\4_SEM\\CourseWork\\Front\\images\\gratis-png-ilustracion-de-trofeo-de-oro-copa-de-torwneo-de-clasoy-royale-thumbnail1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.top_list_button.setIcon(icon3)
        self.top_list_button.setIconSize(QSize(45, 45))
        self.top_list_button.setFlat(True)
        self.input_field = QLineEdit(Dialog)
        self.input_field.setObjectName(u"input_field")
        self.input_field.setGeometry(QRect(20, 170, 391, 31))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.input_field.setFont(font2)
        self.input_field.setStyleSheet(u"")
        self.else_button = QPushButton(Dialog)
        self.else_button.setObjectName(u"else_button")
        self.else_button.setGeometry(QRect(630, 20, 61, 60))
        icon4 = QIcon()
        icon4.addFile(u"D:\\4_SEM\\CourseWork\\Front\\images\\three_dots_vertical_menu_icon_184615.png", QSize(), QIcon.Normal, QIcon.Off)
        self.else_button.setIcon(icon4)
        self.else_button.setIconSize(QSize(40, 40))
        self.else_button.setFlat(True)
        self.other_games_button = QPushButton(Dialog)
        self.other_games_button.setObjectName(u"other_games_button")
        self.other_games_button.setGeometry(QRect(20, 520, 391, 44))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.other_games_button.setFont(font3)
        self.other_games_button.setAutoFillBackground(False)
        self.other_games_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; /* \u0431\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 */\n"
"    color: #333333; /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 1px solid #cccccc; /* \u0441\u0435\u0440\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 5px; /* \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    color: #423232;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f7f7f7; /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.other_games_button.setFlat(False)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 190, 201, 31))
        self.label.setStyleSheet(u" border: 1px solid #ccc;\n"
"border-radius: 5px;        background-color: #F4EDE2;")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 140, 401, 21))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.game_number_label = QLabel(self.layoutWidget)
        self.game_number_label.setObjectName(u"game_number_label")
        self.game_number_label.setStyleSheet(u"color: #423232;")

        self.horizontalLayout.addWidget(self.game_number_label)

        self.date_label = QLabel(self.layoutWidget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setStyleSheet(u" color :#423232;")

        self.horizontalLayout.addWidget(self.date_label)

        self.attempts_label = QLabel(self.layoutWidget)
        self.attempts_label.setObjectName(u"attempts_label")
        self.attempts_label.setStyleSheet(u"color: #423232;")

        self.horizontalLayout.addWidget(self.attempts_label)

        self.hints_label = QLabel(self.layoutWidget)
        self.hints_label.setObjectName(u"hints_label")
        self.hints_label.setStyleSheet(u"color: #423232;")

        self.horizontalLayout.addWidget(self.hints_label)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 20, 71, 70))
        icon5 = QIcon()
        icon5.addFile(u"D:\\4_SEM\\CourseWork\\Front\\images\\png-clipart-computer-icons-communic1ation-message-conversation-others-angle-rectangle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(50, 50))
        self.pushButton.setFlat(True)
        self.new_message = QLabel(Dialog)
        self.new_message.setObjectName(u"new_message")
        self.new_message.setGeometry(QRect(480, 70, 16, 20))
        self.new_message.setPixmap(QPixmap(u"C:/Users/marat/Downloads/imgonline-com-ua-Resize-oLXGTpdLHPtaS.jpg"))
        self.tournament_list_widget = QListWidget(Dialog)
        self.tournament_list_widget.setObjectName(u"tournament_list_widget")
        self.tournament_list_widget.setGeometry(QRect(460, 220, 201, 281))
        self.tournament_list_widget.setFont(font)
        self.tournament_list_widget.setStyleSheet(u"QListWidget {\n"
"    /* \u043e\u0431\u0449\u0438\u0439 \u0441\u0442\u0438\u043b\u044c \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: #F4EDE2;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    padding: 10px;\n"
"    border-bottom: 2px solid #ccc;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"    background-color: #E6DAC3;\n"
"    border-bottom: 2px solid #aaa;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c"
                        "\u0435\u043d\u0442\u0430 */\n"
"    background-color: #C9C4B5;\n"
"    border-bottom: 2px solid #666;\n"
"    color: #333;\n"
"}\n"
"\n"
"QListWidget::item:selected:hover {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"    background-color: #B3A892;\n"
"    border-bottom: 2px solid #444;\n"
"    color: #222;\n"
"}\n"
"")
        self.current_word_list.raise_()
        self.login_button.raise_()
        self.profile_button.raise_()
        self.label_4.raise_()
        self.hint_button.raise_()
        self.input_field.raise_()
        self.else_button.raise_()
        self.other_games_button.raise_()
        self.label.raise_()
        self.layoutWidget.raise_()
        self.top_list_button.raise_()
        self.pushButton.raise_()
        self.new_message.raise_()
        self.tournament_list_widget.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.login_button.setText("")
        self.profile_button.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"LogicOn", None))
        self.hint_button.setText("")
        self.top_list_button.setText("")
        self.input_field.setText("")
        self.else_button.setText("")
        self.other_games_button.setText(QCoreApplication.translate("Dialog", u"\u0414\u0440\u0443\u0433\u0438\u0435 \u0438\u0433\u0440\u044b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"            \u0422\u0443\u0440\u043d\u0438\u0440\u044b", None))
        self.game_number_label.setText(QCoreApplication.translate("Dialog", u"\u0418\u0433\u0440\u0430 \u2116", None))
        self.date_label.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442:", None))
        self.attempts_label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043f\u044b\u0442\u043a\u0438:", None))
        self.hints_label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0438:", None))
        self.pushButton.setText("")
        self.new_message.setText("")
    # retranslateUi

