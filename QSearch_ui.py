# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QSearch.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QSizePolicy, QToolButton, QWidget)

class Ui_Dialog_QSearch(object):
    def setupUi(self, Dialog_QSearch):
        if not Dialog_QSearch.objectName():
            Dialog_QSearch.setObjectName(u"Dialog_QSearch")
        Dialog_QSearch.resize(358, 46)
        self.horizontalLayout = QHBoxLayout(Dialog_QSearch)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(Dialog_QSearch)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(True)

        self.horizontalLayout.addWidget(self.comboBox)

        self.toolButton_Filter = QToolButton(Dialog_QSearch)
        self.toolButton_Filter.setObjectName(u"toolButton_Filter")

        self.horizontalLayout.addWidget(self.toolButton_Filter)

        self.toolButton_Cancel = QToolButton(Dialog_QSearch)
        self.toolButton_Cancel.setObjectName(u"toolButton_Cancel")

        self.horizontalLayout.addWidget(self.toolButton_Cancel)


        self.retranslateUi(Dialog_QSearch)

        QMetaObject.connectSlotsByName(Dialog_QSearch)
    # setupUi

    def retranslateUi(self, Dialog_QSearch):
        Dialog_QSearch.setWindowTitle(QCoreApplication.translate("Dialog_QSearch", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0439 \u0444\u0438\u043b\u044c\u0442\u0440 \u043f\u043e ", None))
        self.toolButton_Filter.setText(QCoreApplication.translate("Dialog_QSearch", u">", None))
        self.toolButton_Cancel.setText(QCoreApplication.translate("Dialog_QSearch", u"X", None))
    # retranslateUi

