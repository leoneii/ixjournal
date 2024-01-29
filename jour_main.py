import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QHeaderView,QTableWidget,QTableWidgetItem
from main import Ui_MainWindow
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
#from PySide6 import QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_Find.clicked.connect(self.findRec)
        self.ui.pushButton_Add.clicked.connect(self.addRec)
        self.ui.pushButton_Change.clicked.connect(self.changeRec)
        self.ui.pushButton_Del.clicked.connect(self.delRec)


        DB = QSqlDatabase.addDatabase('QSQLITE')
        DB.setDatabaseName("jourbd.sqlite")
        DB.open()

        self.updateWidg()


        
    def updateWidg(self):
        query = QSqlQuery()
        qcount = QSqlQuery()
        qcount.exec("SELECT COUNT(*) FROM jtab;")
        qcount.first()
        query.exec("SELECT * FROM jtab ;")
        #query.first()
        r=0
        self.ui.tableWidget.setRowCount(int(qcount.value(0))-1)
        while query.next():
            #self.ui.tableWidget.setItem(r, 0,  QTableWidgetItem(f'line_{r}'))
            self.ui.tableWidget.setItem(r, 0,  QTableWidgetItem(str(query.value(0))))
            self.ui.tableWidget.setItem(r, 1,  QTableWidgetItem(str(query.value(1))))
            self.ui.tableWidget.setItem(r, 2,  QTableWidgetItem(str(query.value(2))))
            self.ui.tableWidget.setItem(r, 3,  QTableWidgetItem(str(query.value(3))))
            self.ui.tableWidget.setItem(r, 4,  QTableWidgetItem(str(query.value(4))))
            self.ui.tableWidget.setItem(r, 5,  QTableWidgetItem(str(query.value(5))))
            self.ui.tableWidget.setItem(r, 6,  QTableWidgetItem(str(query.value(6))))
            self.ui.tableWidget.setItem(r, 7,  QTableWidgetItem(str(query.value(8))))
            r+=1
            if str(query.value(7)) == True: #оплачено
                #self.ui.tableWidget.setPalette #Должно поменять цвет строки
                pass
            if str(query.value(7)) == True: #выдано
                #self.ui.tableWidget. #Должно поменять цвет строки
                pass  


        self.ui.tableWidget.resizeColumnsToContents()

    def findRec(self):
        query = QSqlQuery()
        query.exec("SELECT *  FROM jtab WHERE npp = 1 ;")
        jmodel=QSqlTableModel()
        jmodel.setTable("jtab")
        self.ui.tableView.setModel(jmodel)
        jmodel.setFilter()
        jmodel.select()
        #pass

    def addRec(self):
        adq = QSqlQuery()
        adq.last()
        adq.exec("INSERT INTO jtab DEFAULT VALUES;")
        self.formUpd()

    def changeRec(self):
        pass

    def delRec(self):
        pass  

    def formUpd(self):
        pass
      #  jmod=QSqlTableModel()
      #  jmod.setTable("jtab")
      #  self.ui.tableView.setModel(jmod)
      #  jmod.select()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
