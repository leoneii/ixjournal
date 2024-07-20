import os
import sys
from time import sleep
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QMessageBox, QLabel
from atolMain import Ui_MainWindow
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor
from PySide6.QtCore import QItemSelectionModel
from libfptr10 import IFptr



class MainWindow(QMainWindow):
    fptr = IFptr(r"/home/leone/app/atol10/linux-x64/")
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
    #fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_USB))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_BLUETOOTH)) 
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MACADDRESS,'00:13:43:56:DD:7E')
    fptr.showProperties(IFptr.LIBFPTR_GUI_PARENT_QT,None)
    fptr.applySingleSettings()
    stattext = ""
    if fptr.open()==0:
        stattext="касса подключена, интерфейс открыт"
        print ("касса подключена, интерфейс открыт")
    else:
        stattext="касса не найдена"
        print ("касса не найдена")
        

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        DB = QSqlDatabase.addDatabase('QSQLITE')
        DB.setDatabaseName("susndb.ixdb")
        DB.open()
        self.ui.pushButton_test.clicked.connect(self.test)
        self.ui.closeShift.clicked.connect(self.closeShift,)
        self.ui.listButton.clicked.connect(self.formUpdate)
        self.ui.pushButton_refresh.clicked.connect(self.refresh)
        self.ui.pushButton_Print.clicked.connect(self.print)
        self.statlab = QLabel()
        self.statlab.setText(self.stattext)
        self.statusBar().addWidget(self.statlab)

    def openReceipt(self):
        try:
            self.fptr.closeReceipt()
        except BaseException:
            print (BaseException)

        self.fptr.setParam(1021, "Кассир "+ self.ui.comboBox_kassir.currentText())
        self.fptr.setParam(1203, "462500000000")
        self.fptr.operatorLogin()
        self.fptr.setParam(IFptr.LIBFPTR_PARAM_RECEIPT_TYPE, IFptr.LIBFPTR_RT_SELL)
        return self.fptr.openReceipt()

    def print(self):
        if  self.openReceipt() == 0:
            query= QSqlQuery()
            query.exec("SELECT nomenkl, cost, kolvo, sum FROM spdetail WHERE nomsp='"+self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()+"';")
            while query.next():
                print (str(query.value(0)))
                self.fptr.setParam(IFptr.LIBFPTR_PARAM_COMMODITY_NAME, str(query.value(0)))
                self.fptr.setParam(IFptr.LIBFPTR_PARAM_PRICE, int(query.value(1)))
                self.fptr.setParam(IFptr.LIBFPTR_PARAM_QUANTITY, int(query.value(2)))
                self.fptr.setParam(IFptr.LIBFPTR_PARAM_TAX_TYPE, IFptr.LIBFPTR_TAX_NO)
                self.fptr.setParam(IFptr.LIBFPTR_PARAM_USE_ONLY_TAX_TYPE, True)
                self.fptr.registration()
            self.fptr.closeReceipt()    
        else:
             self.statlab.setText("Ошибка открытия чека")        
        
    def formUpdate(self):
        if self.ui.frameList.geometry().width() <= 300:
            self.setMaximumWidth(29005)
            self.ui.centralwidget.setMaximumWidth(65000)
            for i in range(300):  
                #sleep(0.005)
                self.ui.frameList.setMinimumWidth(300+i)
                self.ui.frameList.setMaximumWidth(300+i)
            print ("1")
        else:
            for i in range(300):  
                #sleep(0.005)
                self.ui.frameList.setMinimumWidth(300-i-1)
                self.ui.frameList.setMaximumWidth(300-i-1)

            self.ui.centralwidget.setMaximumWidth(294)
            self.setMaximumWidth(294)
            #self.updateGeometry()

            print ("2")    

    def refresh(self):
        self.updateList("SELECT kod, nom, date, kontr_name, sum FROM sprint WHERE mode='sprint';", "SELECT COUNT(*) FROM sprint WHERE mode='sprint';")

    def updateList(self, que, quec):
        query = QSqlQuery()
        qcount = QSqlQuery()
        qcount.exec(quec)
        qcount.first()
        query.exec(que)
        #query.first()
        r=0
        self.ui.tableWidget.setRowCount(int(qcount.value(0)))
        while query.next():
            #self.ui.tableWidget.setItem(r, 0,  QTableWidgetItem(f'line_{r}'))
            self.ui.tableWidget.setItem(r, 0,  QTableWidgetItem(str(query.value(0))))
            self.ui.tableWidget.setItem(r, 1,  QTableWidgetItem(str(query.value(1))))
            self.ui.tableWidget.setItem(r, 2,  QTableWidgetItem(str(query.value(2))))
            self.ui.tableWidget.setItem(r, 3,  QTableWidgetItem(str(query.value(3))))
            self.ui.tableWidget.setItem(r, 4,  QTableWidgetItem(str(query.value(4))))
            # if str(query.value(7)) == "True":  # оплачено
            #     for c in range(self.ui.tableWidget.columnCount()):
            #         self.ui.tableWidget.item(r, c).setBackground(QColor(0, 250, 100))  # Должно поменять цвет строки
               # pass
            #f str(query.value(7)) == True: #выдано
                #self.ui.tableWidget. #Должно поменять цвет строки
            #   pass  
            r+=1
        #self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeColumnToContents(0)
        self.ui.tableWidget.resizeColumnToContents(1)
        self.ui.tableWidget.resizeColumnToContents(2)
        self.ui.tableWidget.resizeColumnToContents(3)
        self.ui.tableWidget.resizeColumnToContents(4)

      #  self.ui.tableWidget.setColumnWidth(7, 500)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)




    def closeShift(self):

        self.fptr.setParam(1021, "Кассир "+ self.ui.comboBox_kassir.currentText())
        self.fptr.setParam(1203, "462500000000")
        self.fptr.operatorLogin()
        self.fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_CLOSE_SHIFT)
        self.fptr.report()
        if self.fptr.checkDocumentClosed() != 0:
            self.statlab.setText("Ошибка, смена не закрыта")
        else:
            self.statlab.setText("Смена успешно закрыта")        
            


    def test(self):


        ipAddress = self.fptr.getSingleSetting(IFptr.LIBFPTR_SETTING_IPADDRESS)
        ipPort = self.fptr.getSingleSetting(IFptr.LIBFPTR_SETTING_IPPORT)
        print(str(self.fptr.version())+" "+ipAddress+":"+ipPort)

        self.fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_MODEL_INFO)
        self.fptr.queryData()
        #model           = fptr.getParamInt(IFptr.LIBFPTR_PARAM_MODEL)
        #modelName       = fptr.getParamString(IFptr.LIBFPTR_PARAM_MODEL_NAME)
        #firmwareVersion = fptr.getParamString(IFptr.LIBFPTR_PARAM_UNIT_VERSION)
        print(str(self.fptr.getParamString(IFptr.LIBFPTR_PARAM_MODEL_NAME)))

        self.fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SERIAL_NUMBER)
        self.fptr.queryData()
        print(str(self.fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER)))

        self.fptr.open()
        print(self.fptr.isOpened())

        self.fptr.setParam(1021, "Кассир Иванов И.")
        self.fptr.setParam(1203, "123456789047")
        self.fptr.operatorLogin()

        self.fptr.openShift()

        self.fptr.checkDocumentClosed()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())        
