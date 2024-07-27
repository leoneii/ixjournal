# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1476, 816)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)

        self.horizontalLayout.addWidget(self.tableWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.pushButton_Find = QPushButton(self.frame)
        self.pushButton_Find.setObjectName(u"pushButton_Find")
        self.pushButton_Find.setGeometry(QRect(20, 10, 51, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_Find.sizePolicy().hasHeightForWidth())
        self.pushButton_Find.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u"Filter1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Find.setIcon(icon)
        self.pushButton_Find.setIconSize(QSize(28, 28))
        self.pushButton_Add = QPushButton(self.frame)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        self.pushButton_Add.setGeometry(QRect(20, 110, 121, 51))
        icon1 = QIcon()
        icon1.addFile(u"add.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Add.setIcon(icon1)
        self.pushButton_Change = QPushButton(self.frame)
        self.pushButton_Change.setObjectName(u"pushButton_Change")
        self.pushButton_Change.setGeometry(QRect(20, 170, 121, 51))
        icon2 = QIcon()
        icon2.addFile(u"edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Change.setIcon(icon2)
        self.pushButton_Del = QPushButton(self.frame)
        self.pushButton_Del.setObjectName(u"pushButton_Del")
        self.pushButton_Del.setGeometry(QRect(20, 230, 121, 41))
        icon3 = QIcon()
        icon3.addFile(u"remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Del.setIcon(icon3)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 300, 131, 111))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_Ext = QPushButton(self.groupBox)
        self.pushButton_Ext.setObjectName(u"pushButton_Ext")

        self.verticalLayout.addWidget(self.pushButton_Ext)

        self.pushButton_Pay = QPushButton(self.groupBox)
        self.pushButton_Pay.setObjectName(u"pushButton_Pay")

        self.verticalLayout.addWidget(self.pushButton_Pay)

        self.pushButton_UnFilter = QPushButton(self.frame)
        self.pushButton_UnFilter.setObjectName(u"pushButton_UnFilter")
        self.pushButton_UnFilter.setGeometry(QRect(90, 10, 51, 41))
        sizePolicy1.setHeightForWidth(self.pushButton_UnFilter.sizePolicy().hasHeightForWidth())
        self.pushButton_UnFilter.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u"UnFilter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_UnFilter.setIcon(icon4)
        self.pushButton_UnFilter.setIconSize(QSize(28, 28))
        self.pushButton_UnFilter_All = QPushButton(self.frame)
        self.pushButton_UnFilter_All.setObjectName(u"pushButton_UnFilter_All")
        self.pushButton_UnFilter_All.setGeometry(QRect(20, 60, 121, 41))
        sizePolicy1.setHeightForWidth(self.pushButton_UnFilter_All.sizePolicy().hasHeightForWidth())
        self.pushButton_UnFilter_All.setSizePolicy(sizePolicy1)
        icon5 = QIcon()
        icon5.addFile(u"UnFilterAll.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_UnFilter_All.setIcon(icon5)
        self.pushButton_UnFilter_All.setIconSize(QSize(28, 28))
        self.pushButton_Exit = QPushButton(self.frame)
        self.pushButton_Exit.setObjectName(u"pushButton_Exit")
        self.pushButton_Exit.setGeometry(QRect(10, 700, 131, 41))
        sizePolicy1.setHeightForWidth(self.pushButton_Exit.sizePolicy().hasHeightForWidth())
        self.pushButton_Exit.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u"Exit.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Exit.setIcon(icon6)
        self.pushButton_Exit.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1476, 30))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f/\u043f", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u043a\u0430\u0437\u0430", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None));
#if QT_CONFIG(tooltip)
        self.frame.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438  \u0438\u0437 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Find.setText("")
        self.pushButton_Add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_Change.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_Del.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.groupBox.setTitle("")
        self.pushButton_Ext.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u0442\u044c", None))
        self.pushButton_Pay.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043b\u0430\u0447\u0435\u043d", None))
        self.pushButton_UnFilter.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_UnFilter_All.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u0437\u0430\u043a\u0430\u0437\u044b, \u0432\u043a\u043b\u044e\u0447\u0430\u044f \u0432\u044b\u0434\u0430\u043d\u043d\u044b\u0435 ", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_UnFilter_All.setText("")
        self.pushButton_Exit.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u0436\u0443\u0440\u043d\u0430\u043b\u0430", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

