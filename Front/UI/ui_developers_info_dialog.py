# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_developers_info_dialog.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(511, 390)
        font = QFont()
        font.setBold(False)
        Dialog.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 20, 211, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 161, 141))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u"D:\\4_SEM\\CourseWork\\Front\\images\\imgonline-com-ua-Resize-pC7MFIH98jdszRmhP.jpg"))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 80, 111, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.label_3.setFont(font2)
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 240, 161, 21))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.label_8.setFont(font3)
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(50, 270, 111, 101))
        self.label_9.setPixmap(QPixmap(u"D:\\4_SEM\\CourseWork\\Front\\images\\imgonline-com-ua-Resize-8gBqpN1SYeVwEsWl.jpg"))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(240, 180, 141, 32))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        self.widget.setFont(font4)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setUnderline(True)
        self.label_6.setFont(font5)
        self.label_6.setPixmap(QPixmap(u"D:\\4_SEM\\CourseWork\\Front\\images\\imgonline-com-ua-Resize-F0U2AtAVWqAuX.jpg"))

        self.horizontalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.horizontalLayout.addWidget(self.label_7)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(240, 120, 214, 48))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.verticalLayout.addWidget(self.label_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041e \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u0445", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0429\u0443\u0440 \u041c\u0430\u0440\u0430\u0442", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0438 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.label_9.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"@maratshchur", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u043c\u043e\u0431. \u0442\u0435\u043b\u0435\u0444\u043e\u043d: +375336532182", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"email: marat.shchur@gmail.com", None))
    # retranslateUi

