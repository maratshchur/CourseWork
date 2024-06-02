# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_admin_main_page.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(694, 596)
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
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 20, 221, 51))
        font = QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 26px; /* size of label text */\n"
"    font-weight: bold; /* bold label text */\n"
"}\n"
"")
        self.login_button = QPushButton(Dialog)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(30, 20, 52, 48))
        icon = QIcon()
        icon.addFile(u"D:\\4_SEM\\CourseWork\\Front\\images\\67346.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setIconSize(QSize(40, 40))
        self.login_button.setAutoDefault(False)
        self.login_button.setFlat(True)
        self.users_list = QListWidget(Dialog)
        self.users_list.setObjectName(u"users_list")
        self.users_list.setGeometry(QRect(30, 150, 211, 361))
        self.users_list.setStyleSheet(u"QListWidget {\n"
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
"}\n"
"")
        self.games_list = QListWidget(Dialog)
        self.games_list.setObjectName(u"games_list")
        self.games_list.setGeometry(QRect(250, 150, 211, 361))
        self.games_list.setStyleSheet(u"QListWidget {\n"
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
"}\n"
"")
        self.tournament_list = QListWidget(Dialog)
        self.tournament_list.setObjectName(u"tournament_list")
        self.tournament_list.setGeometry(QRect(470, 150, 211, 361))
        self.tournament_list.setStyleSheet(u"QListWidget {\n"
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
"}\n"
"")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 120, 641, 21))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(240, 520, 461, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.add_game_button = QPushButton(self.layoutWidget1)
        self.add_game_button.setObjectName(u"add_game_button")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.add_game_button.setFont(font1)
        self.add_game_button.setAutoDefault(False)
        self.add_game_button.setFlat(False)

        self.horizontalLayout_2.addWidget(self.add_game_button)

        self.add_tournament_button = QPushButton(self.layoutWidget1)
        self.add_tournament_button.setObjectName(u"add_tournament_button")
        self.add_tournament_button.setFont(font1)
        self.add_tournament_button.setAutoDefault(False)
        self.add_tournament_button.setFlat(False)

        self.horizontalLayout_2.addWidget(self.add_tournament_button)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"LogicOn", None))
        self.login_button.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0433\u0440\u043e\u043a\u043e\u0432", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0433\u0440", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0443\u0440\u043d\u0438\u0440\u043e\u0432", None))
        self.add_game_button.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.add_tournament_button.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0443\u0440\u043d\u0438\u0440", None))
    # retranslateUi

