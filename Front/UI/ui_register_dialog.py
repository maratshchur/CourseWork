# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_register_dialog.ui'
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
        Dialog.resize(468, 496)
        Dialog.setStyleSheet(u"#lineEdit {\n"
"    background-color: #F0F0F0; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    border: 1px solid #CCCCCC; /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 8px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px; /* \u041e\u0442\u0441\u0442\u0443\u043f \u0432\u043d\u0443\u0442\u0440\u0438 \u0432\u0438\u0434\u0436\u0435\u0442\u0430 */\n"
"    color: #333333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-size: 14px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-family: Arial, sans-serif; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"}\n"
"\n"
"#lineEdit:focus {\n"
"    background-color: #FFFFFF; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"    border: 1px solid #4D90FE; /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u0444\u043e"
                        "\u043a\u0443\u0441\u0435 */\n"
"    box-shadow: 0px 0px 5px rgba(77, 144, 254, 0.5); /* \u0422\u0435\u043d\u044c \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"}")
        Dialog.setSizeGripEnabled(False)
        self.registrations_label = QLabel(Dialog)
        self.registrations_label.setObjectName(u"registrations_label")
        self.registrations_label.setGeometry(QRect(90, 10, 341, 51))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(20)
        font.setWeight(QFont.Weight(10))
        font.setItalic(False)
        self.registrations_label.setFont(font)
        self.registrations_label.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";\n"
"font: 87 20pt \"Arial Black\";")
        self.registrations_label.setScaledContents(False)
        self.email_input = QLineEdit(Dialog)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(30, 110, 391, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.email_input.setFont(font1)
        self.password_input = QLineEdit(Dialog)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(30, 260, 391, 41))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 225, 301))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.email_label = QLabel(self.layoutWidget)
        self.email_label.setObjectName(u"email_label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.email_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.email_label)

        self.username_label = QLabel(self.layoutWidget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.username_label)

        self.password_label = QLabel(self.layoutWidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.password_label)

        self.confirm_password_label = QLabel(self.layoutWidget)
        self.confirm_password_label.setObjectName(u"confirm_password_label")
        self.confirm_password_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.confirm_password_label)

        self.username_input = QLineEdit(Dialog)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(30, 190, 391, 41))
        self.username_input.setFont(font1)
        self.register_button = QPushButton(Dialog)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(110, 410, 211, 51))
        font3 = QFont()
        font3.setPointSize(13)
        self.register_button.setFont(font3)
        self.register_button.setStyleSheet(u"QPushButton#register_button {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: #ffffff; /* White */\n"
"    padding: 16px 20px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#register_button:hover {\n"
"    background-color: #3e8e41; /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton#register_button:pressed {\n"
"    background-color: #4CAF50; /* Green on press */\n"
"    border-style: inset;\n"
"}")
        self.confirm_password_input = QLineEdit(Dialog)
        self.confirm_password_input.setObjectName(u"confirm_password_input")
        self.confirm_password_input.setGeometry(QRect(30, 340, 391, 41))
        self.registrations_label.raise_()
        self.layoutWidget.raise_()
        self.register_button.raise_()
        self.confirm_password_input.raise_()
        self.password_input.raise_()
        self.username_input.raise_()
        self.email_input.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.registrations_label.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.email_input.setText("")
        self.email_label.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.username_label.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.password_label.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.confirm_password_label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.username_input.setText("")
        self.register_button.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

