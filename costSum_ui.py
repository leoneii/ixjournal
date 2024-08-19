# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'costSum.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_costSum(object):
    def setupUi(self, costSum):
        if not costSum.objectName():
            costSum.setObjectName(u"costSum")
        costSum.resize(407, 49)
        costSum.setInputMethodHints(Qt.ImhDigitsOnly)
        self.horizontalLayout = QHBoxLayout(costSum)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_costSum = QLineEdit(costSum)
        self.lineEdit_costSum.setObjectName(u"lineEdit_costSum")
        self.lineEdit_costSum.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_costSum.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_costSum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lineEdit_costSum)

        self.label = QLabel(costSum)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.commandLinkButton_endWork = QCommandLinkButton(costSum)
        self.commandLinkButton_endWork.setObjectName(u"commandLinkButton_endWork")

        self.horizontalLayout.addWidget(self.commandLinkButton_endWork)


        self.retranslateUi(costSum)

        QMetaObject.connectSlotsByName(costSum)
    # setupUi

    def retranslateUi(self, costSum):
        costSum.setWindowTitle(QCoreApplication.translate("costSum", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u0442\u043e\u0433\u043e\u0432\u0443\u044e \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0440\u0430\u0431\u043e\u0442", None))
        self.lineEdit_costSum.setInputMask("")
        self.lineEdit_costSum.setText(QCoreApplication.translate("costSum", u"0.00", None))
        self.label.setText(QCoreApplication.translate("costSum", u"\u0420\u0443\u0431\u043b\u0435\u0439", None))
        self.commandLinkButton_endWork.setText(QCoreApplication.translate("costSum", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u044b", None))
    # retranslateUi

