# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_profile_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 241)
        Dialog.setStyleSheet(u"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 61, 61))
        self.label.setPixmap(QPixmap(u"D:\\4_SEM\\CourseWork\\Front\\images\\download.png"))
        self.username_label = QLabel(Dialog)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(100, 20, 281, 51))
        self.username_label.setStyleSheet(u" QLabel {\n"
"	font: 14pt \"Segoe UI\";\n"
"        border: 1px solid #ccc;\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        background-color: #f0f0f0;\n"
"    }\n"
"    QLabel:hover {\n"
"        border-color: #aaa;\n"
"    }")
        self.rating_label = QLabel(Dialog)
        self.rating_label.setObjectName(u"rating_label")
        self.rating_label.setGeometry(QRect(20, 120, 261, 31))
        self.rating_label.setStyleSheet(u"QLabel {\n"
"	font: 14pt \"Segoe UI\";\n"
"        padding: 5px;\n"
"    }\n"
"    QLabel:hover {\n"
"        border-color: #aaa;\n"
"    }")
        self.games_played_label = QLabel(Dialog)
        self.games_played_label.setObjectName(u"games_played_label")
        self.games_played_label.setGeometry(QRect(20, 170, 261, 31))
        self.games_played_label.setStyleSheet(u"QLabel {\n"
"	font: 14pt \"Segoe UI\";\n"
"        padding: 5px;\n"
"    }\n"
"    QLabel:hover {\n"
"        border-color: #aaa;\n"
"    }")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.username_label.setText("")
        self.rating_label.setText("")
        self.games_played_label.setText("")
    # retranslateUi

