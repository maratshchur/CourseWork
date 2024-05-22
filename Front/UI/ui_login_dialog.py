# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"QDialog {\n"
"    background-color: #f0f0f0; /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    font-family: Arial, sans-serif;\n"
"}\n"
"\n"
"/* \u041e\u0431\u0449\u0438\u0439 \u0441\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"QPushButton {\n"
"    background-color: #4CAF50; /* \u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #ffffff; /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none; /* \u0431\u0435\u0437 \u0440\u0430\u043c\u043a\u0438 */\n"
"    border-radius: 5px; /* \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 10px 20px; /* \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px; /* \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    cursor: pointer; /* \u0443\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c \u043c\u044b\u0448\u0438 *"
                        "/\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3e8e41; /* \u0442\u0435\u043c\u043d\u043e-\u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"}\n"
"\n"
"/* \u041e\u0431\u0449\u0438\u0439 \u0441\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043b\u0435\u0439\u0431\u043b\u043e\u0432 */\n"
"QLabel {\n"
"    font-size: 16px; /* \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    color: #333333; /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"}\n"
"\n"
"/* \u041e\u0431\u0449\u0438\u0439 \u0441\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0441\u0442\u0440\u043e\u043a \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit {\n"
"    background-color: #ffffff; /* \u0431\u0435\u043b\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1px solid #cccccc; /* \u0441\u0435\u0440\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 5px; /* \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435"
                        " \u0443\u0433\u043b\u044b */\n"
"    padding: 10px; /* \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px; /* \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    width: 250px; /* \u0448\u0438\u0440\u0438\u043d\u0430 \u043f\u043e\u043b\u044f */\n"
"}")
        self.login_button = QPushButton(Dialog)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(140, 200, 111, 41))
        self.register_button = QPushButton(Dialog)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(70, 240, 251, 41))
        self.register_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent; /* \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: none; /* \u0431\u0435\u0437 \u0440\u0430\u043c\u043a\u0438 */\n"
"    padding: 10px 20px; /* \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px; /* \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    color: #337ab7; /* \u0441\u0438\u043d\u0438\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    text-decoration: underline; /* \u043f\u043e\u0434\u0447\u0435\u0440\u043a\u043d\u0443\u0442\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    cursor: pointer; /* \u0443\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c \u043c\u044b\u0448\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0; /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #23527c; /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u0442\u0435\u043a\u0441\u0442"
                        " */\n"
"    text-decoration: none; /* \u0431\u0435\u0437 \u043f\u043e\u0434\u0447\u0435\u0440\u043a\u0438\u0432\u0430\u043d\u0438\u044f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0; /* \u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #23527c; /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"}")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 30, 274, 154))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.username_label = QLabel(self.layoutWidget)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout.addWidget(self.username_label)

        self.username_input = QLineEdit(self.layoutWidget)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout.addWidget(self.username_input)

        self.password_label = QLabel(self.layoutWidget)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout.addWidget(self.password_label)

        self.password_input = QLineEdit(self.layoutWidget)
        self.password_input.setObjectName(u"password_input")

        self.verticalLayout.addWidget(self.password_input)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.login_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.register_button.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.username_label.setText(QCoreApplication.translate("Dialog", u" Email", None))
        self.password_label.setText(QCoreApplication.translate("Dialog", u"Password", None))
    # retranslateUi

