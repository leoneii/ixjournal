# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finddial.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_fDial(object):
    def setupUi(self, fDial):
        if not fDial.objectName():
            fDial.setObjectName(u"fDial")
        fDial.resize(400, 300)
        self.buttonBox = QDialogButtonBox(fDial)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_date = QLabel(fDial)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(20, 20, 91, 16))
        self.label_date_2 = QLabel(fDial)
        self.label_date_2.setObjectName(u"label_date_2")
        self.label_date_2.setGeometry(QRect(240, 20, 21, 16))
        self.label_date_3 = QLabel(fDial)
        self.label_date_3.setObjectName(u"label_date_3")
        self.label_date_3.setGeometry(QRect(20, 60, 91, 16))
        self.lineEdit_numbZak = QLineEdit(fDial)
        self.lineEdit_numbZak.setObjectName(u"lineEdit_numbZak")
        self.lineEdit_numbZak.setGeometry(QRect(122, 60, 101, 22))
        self.label_date_4 = QLabel(fDial)
        self.label_date_4.setObjectName(u"label_date_4")
        self.label_date_4.setGeometry(QRect(20, 100, 81, 16))
        self.comboBox_cont = QComboBox(fDial)
        self.comboBox_cont.setObjectName(u"comboBox_cont")
        self.comboBox_cont.setGeometry(QRect(100, 90, 291, 30))
        self.comboBox_cont.setEditable(True)
        self.dateEdit_Start = QDateEdit(fDial)
        self.dateEdit_Start.setObjectName(u"dateEdit_Start")
        self.dateEdit_Start.setGeometry(QRect(120, 10, 110, 32))
        self.dateEdit_Start.setCalendarPopup(True)
        self.dateEdit_End = QDateEdit(fDial)
        self.dateEdit_End.setObjectName(u"dateEdit_End")
        self.dateEdit_End.setGeometry(QRect(260, 10, 110, 32))
        self.dateEdit_End.setCalendarPopup(True)

        self.retranslateUi(fDial)
        self.buttonBox.accepted.connect(fDial.accept)
        self.buttonBox.rejected.connect(fDial.reject)

        QMetaObject.connectSlotsByName(fDial)
    # setupUi

    def retranslateUi(self, fDial):
        fDial.setWindowTitle(QCoreApplication.translate("fDial", u"Dialog", None))
        self.label_date.setText(QCoreApplication.translate("fDial", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430 \u0441", None))
        self.label_date_2.setText(QCoreApplication.translate("fDial", u"\u043f\u043e", None))
        self.label_date_3.setText(QCoreApplication.translate("fDial", u"\u043d\u043e\u043c\u0435\u0440 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_date_4.setText(QCoreApplication.translate("fDial", u"\u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
    # retranslateUi

