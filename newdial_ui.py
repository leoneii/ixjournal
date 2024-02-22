# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newdial.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(534, 384)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(170, 340, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_dat = QLabel(Dialog)
        self.label_dat.setObjectName(u"label_dat")
        self.label_dat.setGeometry(QRect(20, 10, 49, 16))
        font = QFont()
        font.setPointSize(11)
        self.label_dat.setFont(font)
        self.label_numZak = QLabel(Dialog)
        self.label_numZak.setObjectName(u"label_numZak")
        self.label_numZak.setGeometry(QRect(20, 40, 101, 16))
        self.label_numZak.setFont(font)
        self.label_zak = QLabel(Dialog)
        self.label_zak.setObjectName(u"label_zak")
        self.label_zak.setGeometry(QRect(20, 100, 101, 16))
        self.label_zak.setFont(font)
        self.label_phone = QLabel(Dialog)
        self.label_phone.setObjectName(u"label_phone")
        self.label_phone.setGeometry(QRect(20, 70, 61, 16))
        self.label_phone.setFont(font)
        self.label_prim = QLabel(Dialog)
        self.label_prim.setObjectName(u"label_prim")
        self.label_prim.setGeometry(QRect(20, 250, 101, 16))
        self.label_prim.setFont(font)
        self.label_cost = QLabel(Dialog)
        self.label_cost.setObjectName(u"label_cost")
        self.label_cost.setGeometry(QRect(20, 220, 101, 16))
        self.label_cost.setFont(font)
        self.label_descr = QLabel(Dialog)
        self.label_descr.setObjectName(u"label_descr")
        self.label_descr.setGeometry(QRect(20, 130, 81, 16))
        self.label_descr.setFont(font)
        self.checkBox_costYN = QCheckBox(Dialog)
        self.checkBox_costYN.setObjectName(u"checkBox_costYN")
        self.checkBox_costYN.setGeometry(QRect(430, 220, 91, 20))
        self.checkBox_costYN.setFont(font)
        self.checkBox_end = QCheckBox(Dialog)
        self.checkBox_end.setObjectName(u"checkBox_end")
        self.checkBox_end.setGeometry(QRect(430, 310, 91, 20))
        self.checkBox_end.setFont(font)
        self.lineEdit_dat = QLineEdit(Dialog)
        self.lineEdit_dat.setObjectName(u"lineEdit_dat")
        self.lineEdit_dat.setGeometry(QRect(140, 10, 113, 22))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_dat.setFont(font1)
        self.lineEdit_numZak = QLineEdit(Dialog)
        self.lineEdit_numZak.setObjectName(u"lineEdit_numZak")
        self.lineEdit_numZak.setGeometry(QRect(140, 40, 113, 22))
        self.lineEdit_numZak.setFont(font1)
        self.lineEdit_phone = QLineEdit(Dialog)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")
        self.lineEdit_phone.setGeometry(QRect(140, 70, 113, 22))
        self.lineEdit_phone.setFont(font1)
        self.lineEdit_nameZak = QLineEdit(Dialog)
        self.lineEdit_nameZak.setObjectName(u"lineEdit_nameZak")
        self.lineEdit_nameZak.setGeometry(QRect(140, 100, 371, 22))
        self.lineEdit_nameZak.setFont(font1)
        self.textEdit_descryption = QTextEdit(Dialog)
        self.textEdit_descryption.setObjectName(u"textEdit_descryption")
        self.textEdit_descryption.setGeometry(QRect(140, 130, 371, 71))
        self.lineEdit_costSum = QLineEdit(Dialog)
        self.lineEdit_costSum.setObjectName(u"lineEdit_costSum")
        self.lineEdit_costSum.setGeometry(QRect(140, 220, 113, 22))
        self.lineEdit_costSum.setFont(font1)
        self.textEdit_prim = QTextEdit(Dialog)
        self.textEdit_prim.setObjectName(u"textEdit_prim")
        self.textEdit_prim.setGeometry(QRect(140, 250, 371, 51))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_dat.setText(QCoreApplication.translate("Dialog", u"\u0434\u0430\u0442\u0430", None))
        self.label_numZak.setText(QCoreApplication.translate("Dialog", u"\u043d\u043e\u043c\u0435\u0440 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_zak.setText(QCoreApplication.translate("Dialog", u"\u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
        self.label_phone.setText(QCoreApplication.translate("Dialog", u"\u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_prim.setText(QCoreApplication.translate("Dialog", u"\u043f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None))
        self.label_cost.setText(QCoreApplication.translate("Dialog", u"\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.label_descr.setText(QCoreApplication.translate("Dialog", u"\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.checkBox_costYN.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u043b\u0430\u0447\u0435\u043d", None))
        self.checkBox_end.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d", None))
        self.lineEdit_dat.setText("")
        self.lineEdit_numZak.setText("")
        self.lineEdit_phone.setText("")
        self.lineEdit_nameZak.setText("")
        self.lineEdit_costSum.setText("")
    # retranslateUi

