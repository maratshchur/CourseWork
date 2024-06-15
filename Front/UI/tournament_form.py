# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tournament_form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(362, 452)
        Form.setStyleSheet(u"QWidget{\n"
"background-color: #FFFBF5; /* \u0431\u0435\u043b\u044b\u0439 \u0431\u044d\u043a\u0433\u0440\u0430\u0443\u043d\u0434 */\n"
"}\n"
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
        self.input_field = QLineEdit(Form)
        self.input_field.setObjectName(u"input_field")
        self.input_field.setGeometry(QRect(10, 50, 341, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.input_field.setFont(font)
        self.current_word_list = QListWidget(Form)
        self.current_word_list.setObjectName(u"current_word_list")
        self.current_word_list.setGeometry(QRect(10, 90, 341, 331))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.current_word_list.setFont(font1)
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
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 201, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.input_field.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043f\u044b\u0442\u043a\u0438:", None))
    # retranslateUi

