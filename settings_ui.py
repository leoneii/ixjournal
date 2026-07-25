# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QButtonGroup, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(360, 260)
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_Messaging = QGroupBox(SettingsDialog)
        self.groupBox_Messaging.setObjectName(u"groupBox_Messaging")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_Messaging)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_iDigital = QRadioButton(self.groupBox_Messaging)
        self.buttonGroup_Messaging = QButtonGroup(SettingsDialog)
        self.buttonGroup_Messaging.setObjectName(u"buttonGroup_Messaging")
        self.buttonGroup_Messaging.addButton(self.radioButton_iDigital)
        self.radioButton_iDigital.setObjectName(u"radioButton_iDigital")

        self.verticalLayout_2.addWidget(self.radioButton_iDigital)

        self.radioButton_SmsPilot = QRadioButton(self.groupBox_Messaging)
        self.buttonGroup_Messaging.addButton(self.radioButton_SmsPilot)
        self.radioButton_SmsPilot.setObjectName(u"radioButton_SmsPilot")

        self.verticalLayout_2.addWidget(self.radioButton_SmsPilot)


        self.verticalLayout.addWidget(self.groupBox_Messaging)

        self.groupBox_Printer = QGroupBox(SettingsDialog)
        self.groupBox_Printer.setObjectName(u"groupBox_Printer")
        self.formLayout = QFormLayout(self.groupBox_Printer)
        self.formLayout.setObjectName(u"formLayout")
        self.label_PrinterAddress = QLabel(self.groupBox_Printer)
        self.label_PrinterAddress.setObjectName(u"label_PrinterAddress")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_PrinterAddress)

        self.lineEdit_PrinterAddress = QLineEdit(self.groupBox_Printer)
        self.lineEdit_PrinterAddress.setObjectName(u"lineEdit_PrinterAddress")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_PrinterAddress)

        self.label_PrinterDensity = QLabel(self.groupBox_Printer)
        self.label_PrinterDensity.setObjectName(u"label_PrinterDensity")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_PrinterDensity)

        self.spinBox_PrinterDensity = QSpinBox(self.groupBox_Printer)
        self.spinBox_PrinterDensity.setObjectName(u"spinBox_PrinterDensity")
        self.spinBox_PrinterDensity.setMinimum(1)
        self.spinBox_PrinterDensity.setMaximum(3)
        self.spinBox_PrinterDensity.setValue(3)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_PrinterDensity)

        self.label_PrinterLength = QLabel(self.groupBox_Printer)
        self.label_PrinterLength.setObjectName(u"label_PrinterLength")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_PrinterLength)

        self.comboBox_PrinterLength = QComboBox(self.groupBox_Printer)
        self.comboBox_PrinterLength.addItem("")
        self.comboBox_PrinterLength.addItem("")
        self.comboBox_PrinterLength.setObjectName(u"comboBox_PrinterLength")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox_PrinterLength)


        self.verticalLayout.addWidget(self.groupBox_Printer)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox_Messaging.setTitle(QCoreApplication.translate("SettingsDialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439 \u043e \u0433\u043e\u0442\u043e\u0432\u043d\u043e\u0441\u0442\u0438 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.radioButton_iDigital.setText(QCoreApplication.translate("SettingsDialog", u"iDigital", None))
        self.radioButton_SmsPilot.setText(QCoreApplication.translate("SettingsDialog", u"SMSPilot", None))
        self.groupBox_Printer.setTitle(QCoreApplication.translate("SettingsDialog", u"\u041f\u0440\u0438\u043d\u0442\u0435\u0440 \u044d\u0442\u0438\u043a\u0435\u0442\u043e\u043a (Niimbot)", None))
        self.label_PrinterAddress.setText(QCoreApplication.translate("SettingsDialog", u"Bluetooth-\u0430\u0434\u0440\u0435\u0441", None))
        self.lineEdit_PrinterAddress.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"AA:BB:CC:DD:EE:FF", None))
        self.label_PrinterDensity.setText(QCoreApplication.translate("SettingsDialog", u"\u041f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u0435\u0447\u0430\u0442\u0438", None))
        self.label_PrinterLength.setText(QCoreApplication.translate("SettingsDialog", u"\u0414\u043b\u0438\u043d\u0430 \u044d\u0442\u0438\u043a\u0435\u0442\u043a\u0438", None))
        self.comboBox_PrinterLength.setItemText(0, QCoreApplication.translate("SettingsDialog", u"30 \u043c\u043c", None))
        self.comboBox_PrinterLength.setItemText(1, QCoreApplication.translate("SettingsDialog", u"40 \u043c\u043c", None))

    # retranslateUi

