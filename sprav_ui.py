# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sprav.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_spDialog(object):
    def setupUi(self, spDialog):
        if not spDialog.objectName():
            spDialog.setObjectName(u"spDialog")
        spDialog.resize(705, 489)
        self.buttonBox = QDialogButtonBox(spDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(530, 460, 156, 24))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.frame = QFrame(spDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 151, 441))
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_zakaz = QPushButton(self.frame)
        self.pushButton_zakaz.setObjectName(u"pushButton_zakaz")
        self.pushButton_zakaz.setGeometry(QRect(4, 10, 111, 24))
        self.frame_2 = QFrame(spDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(145, 9, 411, 441))
        self.frame_2.setMaximumSize(QSize(420, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.tableView = QTableView(self.frame_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 30, 391, 391))
        self.tableView.setMaximumSize(QSize(800, 16777215))
        self.label_selSprav = QLabel(self.frame_2)
        self.label_selSprav.setObjectName(u"label_selSprav")
        self.label_selSprav.setGeometry(QRect(8, 10, 391, 20))
        self.frame_3 = QFrame(spDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(555, 9, 141, 441))
        self.frame_3.setMaximumSize(QSize(200, 16777215))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_Edit = QPushButton(self.frame_3)
        self.pushButton_Edit.setObjectName(u"pushButton_Edit")
        self.pushButton_Edit.setGeometry(QRect(10, 40, 121, 24))
        icon = QIcon()
        icon.addFile(u"image/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Edit.setIcon(icon)
        self.pushButton_Add = QPushButton(self.frame_3)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        self.pushButton_Add.setGeometry(QRect(10, 10, 121, 24))
        icon1 = QIcon()
        icon1.addFile(u"image/add.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Add.setIcon(icon1)
        self.pushButton_Del = QPushButton(self.frame_3)
        self.pushButton_Del.setObjectName(u"pushButton_Del")
        self.pushButton_Del.setGeometry(QRect(10, 70, 121, 24))
        icon2 = QIcon()
        icon2.addFile(u"image/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Del.setIcon(icon2)

        self.retranslateUi(spDialog)
        self.buttonBox.accepted.connect(spDialog.accept)
        self.buttonBox.rejected.connect(spDialog.reject)

        QMetaObject.connectSlotsByName(spDialog)
    # setupUi

    def retranslateUi(self, spDialog):
        spDialog.setWindowTitle(QCoreApplication.translate("spDialog", u"Dialog", None))
        self.pushButton_zakaz.setText(QCoreApplication.translate("spDialog", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0438", None))
        self.label_selSprav.setText(QCoreApplication.translate("spDialog", u"TextLabel", None))
        self.pushButton_Edit.setText(QCoreApplication.translate("spDialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_Add.setText(QCoreApplication.translate("spDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_Del.setText(QCoreApplication.translate("spDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

