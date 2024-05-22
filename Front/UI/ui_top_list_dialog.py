# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_top_list_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(298, 343)
        Dialog.setStyleSheet(u"/* Style the dialog window */\n"
"QDialog {\n"
"    background-color: #f0f0f0; /* light gray background */\n"
"    border: 1px solid #ccc; /* thin gray border */\n"
"    border-radius: 5px; /* rounded corners */\n"
"}\n"
"\n"
"/* Style the label */\n"
"QLabel {\n"
"    font-size: 18px; /* larger font size */\n"
"    font-weight: bold; /* bold font */\n"
"    color: #333; /* dark gray text color */\n"
"}\n"
"\n"
"/* Style the list widget */\n"
"QListWidget {\n"
"    background-color: #fff; /* white background */\n"
"    border: 1px solid #ddd; /* thin gray border */\n"
"    border-radius: 5px; /* rounded corners */\n"
"}\n"
"\n"
"/* Style the list items */\n"
"QListWidgetItem {\n"
"    padding: 10px; /* add some padding to the list items */\n"
"    border-bottom: 1px solid #ccc; /* thin gray border between list items */\n"
"}\n"
"\n"
"QListWidgetItem:hover {\n"
"    background-color: #f0f0f0; /* light gray background on hover */\n"
"}\n"
"\n"
"QListWidgetItem:selected {\n"
"    background-color: #ccc; /* gray b"
                        "ackground on selection */\n"
"    color: #333; /* dark gray text color on selection */\n"
"}")
        self.top_list = QListWidget(Dialog)
        self.top_list.setObjectName(u"top_list")
        self.top_list.setGeometry(QRect(20, 70, 256, 241))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 161, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041b\u0443\u0447\u0448\u0438\u0435 \u0438\u0433\u0440\u043e\u043a\u0438", None))
    # retranslateUi

