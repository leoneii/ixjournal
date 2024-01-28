import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main import Ui_MainWindow
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

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

        model=QSqlTableModel()
        model.setTable("jtab")
        self.ui.tableView.setModel(model)
        model.select()

    def findRec(self):
        pass

    def addRec(self):
        pass  

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
    sys.exit(app.exec_())
