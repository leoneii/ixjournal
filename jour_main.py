import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QHeaderView
from main import Ui_MainWindow
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

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

        jmodel=QSqlTableModel()
        jmodel.setTable("jtab")
        self.ui.tableView.setModel(jmodel)
        jmodel.select()

        header = self.ui.tableView.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.ResizeToContents)

        


    def findRec(self):
        pass

    def addRec(self):
        adq=QSqlQuery()
        adq.exec("INSERT INTO jtab DEFAULT VALUES;")

    def changeRec(self):
        pass

    def delRec(self):
        pass  

    def formUpd(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
