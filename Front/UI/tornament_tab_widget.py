# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tornament_tab_widget.ui'
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
    QListWidgetItem, QSizePolicy, QTabWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 543)
        Dialog.setStyleSheet(u"QDialog{\n"
"background-color: #FFFBF5; /* \u0431\u0435\u043b\u044b\u0439 \u0431\u044d\u043a\u0433\u0440\u0430\u0443\u043d\u0434 */\n"
"}\n"
"QLabel {\n"
"    font-size: 14px; /* size of label text */\n"
"    font-weight: bold; /* bold label text */\n"
"}\n"
"\n"
"")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 50, 451, 511))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: None;\n"
"    background-color: #FFFBF5; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"    margin-top: 0px; /* adjust the top margin to make tabs start higher */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    font: bold 10pt \"Segoe UI\"; /* new font and bold text */\n"
"    background-color: #F4EDE2; /* \u0446\u0432\u0435\u0442 \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 */\n"
"    color: #333;\n"
"    padding: 5px 10px; /* adjust the padding to make tabs start higher */\n"
"    border: 1px solid #F4EDE2;\n"
"    border-radius: 5px 5px 0 0;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    font: bold 10pt \"Segoe UI\"; /* new font and bold text */\n"
"    background-color: #C9C4B5; /* \u0446\u0432\u0435\u0442 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 */\n"
"    color: #333;\n"
"    border-bottom: 2px solid #C9C4B5;\n"
"    box-shadow: 0 0 10px rgba(255, 193, 7, 0.5);\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    font: bold 10pt \"Segoe UI\"; /* new font and bold text */\n"
"    background-color: #E6DAC3; /* \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d"
                        "\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"    color: #333;\n"
"    border-bottom: 1px solid #E6DAC3;\n"
"}\n"
"\n"
"QTabBar::tab:disabled {\n"
"    font: bold 10pt \"Segoe UI\"; /* new font and bold text */\n"
"    background-color: #ccc; /* \u0446\u0432\u0435\u0442 \u043d\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 */\n"
"    color: #666;\n"
"    border-bottom: 1px solid #ccc;\n"
"}")
        self.title_label = QLabel(Dialog)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(100, 10, 521, 31))
        self.title_label.setStyleSheet(u"\n"
"QLabel {\n"
"    font-size: 18px; /* size of label text */\n"
"    font-weight: bold; /* bold label text */\n"
"}\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 120, 221, 20))
        self.label.setStyleSheet(u"\n"
"QLabel {\n"
"    font-size: 14px; /* size of label text */\n"
"    font-weight: bold; /* bold label text */\n"
"}\n"
"")
        self.standings_list = QListWidget(Dialog)
        self.standings_list.setObjectName(u"standings_list")
        self.standings_list.setGeometry(QRect(420, 150, 221, 331))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.standings_list.setFont(font)
        self.standings_list.setStyleSheet(u"QListWidget {\n"
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
        self.remaining_time_label = QLabel(Dialog)
        self.remaining_time_label.setObjectName(u"remaining_time_label")
        self.remaining_time_label.setGeometry(QRect(490, 510, 181, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0443\u0440\u043d\u0438\u0440\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0440\u043d\u0438\u0440\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.remaining_time_label.setText("")
    # retranslateUi

