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
        Dialog.setStyleSheet(u"QDiaog {\n"
"    background-color: #F0F0F0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */}\n"
"\n"
"QLabel {\n"
"    font-size: 14px; /* size of label text */\n"
"    font-weight: bold; /* bold label text */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #ccc; /* light gray border for input fields */\n"
"    border-radius: 5px; /* rounded corners for input fields */\n"
"    padding: 5px; /* padding for input fields */\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none; /* no border for buttons */\n"
"    border-radius: 5px; /* rounded corners for buttons */\n"
"    padding: 10px 20px; /* padding for buttons */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0; /* light gray background on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d0d0d0; /* dark gray background on press */\n"
"}")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 130, 501, 29))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.game_number_label = QLabel(self.layoutWidget)
        self.game_number_label.setObjectName(u"game_number_label")

        self.horizontalLayout.addWidget(self.game_number_label)

        self.date_label = QLabel(self.layoutWidget)
        self.date_label.setObjectName(u"date_label")

        self.horizontalLayout.addWidget(self.date_label)

        self.attempts_label = QLabel(self.layoutWidget)
        self.attempts_label.setObjectName(u"attempts_label")

        self.horizontalLayout.addWidget(self.attempts_label)

        self.hints_label = QLabel(self.layoutWidget)
        self.hints_label.setObjectName(u"hints_label")

        self.horizontalLayout.addWidget(self.hints_label)

        self.current_word_list = QListWidget(Dialog)
        self.current_word_list.setObjectName(u"current_word_list")
        self.current_word_list.setGeometry(QRect(20, 220, 431, 281))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.current_word_list.setFont(font)
        self.current_word_list.setStyleSheet(u"QListWidget {\n"
"    /* \u043e\u0431\u0449\u0438\u0439 \u0441\u0442\u0438\u043b\u044c \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: #f0f0f0;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #ccc;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    background-color: #0078ff;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u0441\u043f\u0438\u0441\u043a\u0430 \u043f\u0440\u0438 \u043d"
                        "\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"    background-color: #f7f7f7;\n"
"}\n"
"\n"
"QListWidget::item:disabled {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u043d\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    color: #808080;\n"
"}")
        self.login_button = QPushButton(Dialog)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(21, 31, 52, 48))
        icon = QIcon()
        icon.addFile(u"../images/67346.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setIconSize(QSize(40, 40))
        self.login_button.setFlat(True)
        self.profile_button = QPushButton(Dialog)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setGeometry(QRect(570, 30, 61, 51))
        icon1 = QIcon()
        icon1.addFile(u"../images/download1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_button.setIcon(icon1)
        self.profile_button.setIconSize(QSize(45, 45))
        self.profile_button.setFlat(True)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 30, 221, 51))
        font1 = QFont()
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 26px; /* size of label text */\n"
"    font-weight: bold; /* bold label text */\n"
"}\n"
"")
        self.hint_button = QPushButton(Dialog)
        self.hint_button.setObjectName(u"hint_button")
        self.hint_button.setGeometry(QRect(580, 520, 75, 71))
        icon2 = QIcon()
        icon2.addFile(u"../images/png-clipart-computer-icons-idea-brainstorming-others-miscellaneous-image-file-formats.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hint_button.setIcon(icon2)
        self.hint_button.setIconSize(QSize(50, 50))
        self.hint_button.setFlat(True)
        self.top_list_button = QPushButton(Dialog)
        self.top_list_button.setObjectName(u"top_list_button")
        self.top_list_button.setGeometry(QRect(500, 30, 51, 51))
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/marat/Downloads/imgonline-com-ua-Resize-nB8vUTYJ.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.top_list_button.setIcon(icon3)
        self.top_list_button.setIconSize(QSize(50, 50))
        self.top_list_button.setFlat(True)
        self.input_field = QLineEdit(Dialog)
        self.input_field.setObjectName(u"input_field")
        self.input_field.setGeometry(QRect(20, 170, 431, 31))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.input_field.setFont(font2)
        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 527, 491, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.other_games_button = QPushButton(self.layoutWidget1)
        self.other_games_button.setObjectName(u"other_games_button")
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
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f7f7f7; /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.other_games_button.setFlat(False)

        self.horizontalLayout_2.addWidget(self.other_games_button)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.else_button = QPushButton(Dialog)
        self.else_button.setObjectName(u"else_button")
        self.else_button.setGeometry(QRect(630, 30, 61, 51))
        icon4 = QIcon()
        icon4.addFile(u"../images/three_dots_vertical_menu_icon_184615.png", QSize(), QIcon.Normal, QIcon.Off)
        self.else_button.setIcon(icon4)
        self.else_button.setIconSize(QSize(40, 40))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.game_number_label.setText(QCoreApplication.translate("Dialog", u"\u0418\u0433\u0440\u0430 \u2116", None))
        self.date_label.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442:", None))
        self.attempts_label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043f\u044b\u0442\u043a\u0438:", None))
        self.hints_label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0438:", None))
        self.login_button.setText("")
        self.profile_button.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"LogicOn", None))
        self.hint_button.setText("")
        self.top_list_button.setText("")
        self.input_field.setText("")
        self.other_games_button.setText(QCoreApplication.translate("Dialog", u"\u0414\u0440\u0443\u0433\u0438\u0435 \u0438\u0433\u0440\u044b", None))
        self.else_button.setText("")
    # retranslateUi

