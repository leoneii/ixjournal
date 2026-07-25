# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atolMain.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(889, 523)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(265, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(250, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_main = QLabel(self.frame_3)
        self.label_main.setObjectName(u"label_main")
        font = QFont()
        font.setPointSize(20)
        self.label_main.setFont(font)

        self.verticalLayout_4.addWidget(self.label_main)

        self.label_mini = QLabel(self.frame_3)
        self.label_mini.setObjectName(u"label_mini")

        self.verticalLayout_4.addWidget(self.label_mini)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox_kassir = QComboBox(self.frame_2)
        self.comboBox_kassir.addItem("")
        self.comboBox_kassir.addItem("")
        self.comboBox_kassir.setObjectName(u"comboBox_kassir")

        self.verticalLayout_2.addWidget(self.comboBox_kassir)

        self.openShift = QPushButton(self.frame_2)
        self.openShift.setObjectName(u"openShift")

        self.verticalLayout_2.addWidget(self.openShift)

        self.listButton = QPushButton(self.frame_2)
        self.listButton.setObjectName(u"listButton")

        self.verticalLayout_2.addWidget(self.listButton)

        self.closeShift = QPushButton(self.frame_2)
        self.closeShift.setObjectName(u"closeShift")

        self.verticalLayout_2.addWidget(self.closeShift)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.pushButton_test = QPushButton(self.frame_2)
        self.pushButton_test.setObjectName(u"pushButton_test")

        self.verticalLayout_2.addWidget(self.pushButton_test)

        self.pushButton_refresh = QPushButton(self.frame_2)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.verticalLayout_2.addWidget(self.pushButton_refresh)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setMinimumSize(QSize(250, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.exitButton = QPushButton(self.frame_4)
        self.exitButton.setObjectName(u"exitButton")

        self.verticalLayout_3.addWidget(self.exitButton)


        self.verticalLayout_5.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

        self.frameList = QFrame(self.centralwidget)
        self.frameList.setObjectName(u"frameList")
        sizePolicy.setHeightForWidth(self.frameList.sizePolicy().hasHeightForWidth())
        self.frameList.setSizePolicy(sizePolicy)
        self.frameList.setMinimumSize(QSize(0, 0))
        self.frameList.setFrameShape(QFrame.StyledPanel)
        self.frameList.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameList)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.frameList)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.pushButton_Print = QPushButton(self.frameList)
        self.pushButton_Print.setObjectName(u"pushButton_Print")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_Print.sizePolicy().hasHeightForWidth())
        self.pushButton_Print.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.pushButton_Print)


        self.horizontalLayout.addWidget(self.frameList)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 889, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_main.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0430 \u0417\u0430\u043a\u0440\u044b\u0442\u0430!", None))
        self.label_mini.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.comboBox_kassir.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0413\u043d\u0435\u0437\u0434\u0438\u043b\u043e\u0432\u0430 \u041e.\u0418.", None))
        self.comboBox_kassir.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0447\u0435\u043f\u0443\u0440\u0435\u043d\u043a\u043e \u042d.\u0412.", None))

        self.openShift.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u0438\u0435 \u0441\u043c\u0435\u043d\u044b", None))
        self.listButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0439 =>", None))
        self.closeShift.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u0438\u0435 \u0441\u043c\u0435\u043d\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_test.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043d\u0430\u043a\u043b.", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c.\u043d\u0430\u043a\u043b.", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None));
        self.pushButton_Print.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0447\u0435\u043a\u0430", None))
    # retranslateUi

