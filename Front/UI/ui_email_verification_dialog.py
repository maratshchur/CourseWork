# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_email_verification_dialog.ui'
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
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

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
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 381, 41))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0439 \u0441\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043b\u0435\u0439\u0431\u043b\u043e\u0432 */\n"
"QLabel {\n"
"    font-size: 20px; /* \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    color: #333333; /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"}")
        self.instructions_text = QTextBrowser(Dialog)
        self.instructions_text.setObjectName(u"instructions_text")
        self.instructions_text.setGeometry(QRect(50, 80, 311, 61))
        self.instructions_text.setStyleSheet(u"QTextBrowser {\n"
"    border: none; /* remove border */\n"
"    background-color: #f0f0f0; /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    font-family: Arial, sans-serif;\n"
"    padding: 5px; /* add some padding around the text */\n"
"}\n"
"\n"
"\n"
"QTextBrowser::te {\n"
"    /* style for the text area */\n"
"    padding: 5px; /* add some padding around the text */\n"
"}")
        self.first_digit_input = QLineEdit(Dialog)
        self.first_digit_input.setObjectName(u"first_digit_input")
        self.first_digit_input.setGeometry(QRect(20, 160, 51, 41))
        self.first_digit_input.setFont(font)
        self.first_digit_input.setMaxLength(1)
        self.second_digit_input = QLineEdit(Dialog)
        self.second_digit_input.setObjectName(u"second_digit_input")
        self.second_digit_input.setGeometry(QRect(80, 160, 51, 41))
        self.second_digit_input.setFont(font)
        self.second_digit_input.setMaxLength(1)
        self.third_digit_input = QLineEdit(Dialog)
        self.third_digit_input.setObjectName(u"third_digit_input")
        self.third_digit_input.setGeometry(QRect(140, 160, 51, 41))
        self.third_digit_input.setFont(font)
        self.third_digit_input.setMaxLength(1)
        self.fourth_digit_input = QLineEdit(Dialog)
        self.fourth_digit_input.setObjectName(u"fourth_digit_input")
        self.fourth_digit_input.setGeometry(QRect(200, 160, 51, 41))
        self.fourth_digit_input.setFont(font)
        self.fourth_digit_input.setMaxLength(1)
        self.fifth_digit_input = QLineEdit(Dialog)
        self.fifth_digit_input.setObjectName(u"fifth_digit_input")
        self.fifth_digit_input.setGeometry(QRect(260, 160, 51, 41))
        self.fifth_digit_input.setFont(font)
        self.fifth_digit_input.setMaxLength(1)
        self.sixth_digit_input = QLineEdit(Dialog)
        self.sixth_digit_input.setObjectName(u"sixth_digit_input")
        self.sixth_digit_input.setGeometry(QRect(320, 160, 51, 41))
        self.sixth_digit_input.setFont(font)
        self.sixth_digit_input.setMaxLength(1)
        self.submit_button = QPushButton(Dialog)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(120, 210, 141, 41))
        self.resend_otp_button = QPushButton(Dialog)
        self.resend_otp_button.setObjectName(u"resend_otp_button")
        self.resend_otp_button.setGeometry(QRect(90, 250, 221, 41))
        self.resend_otp_button.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u043f\u043e\u0447\u0442\u044b", None))
        self.instructions_text.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial','sans-serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.first_digit_input.setText("")
        self.second_digit_input.setText("")
        self.submit_button.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.resend_otp_button.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u0434 \u043f\u043e\u0432\u0442\u043e\u0440\u043d\u043e", None))
    # retranslateUi

