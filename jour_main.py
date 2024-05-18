import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QMessageBox, QDialog
from main_ui import Ui_MainWindow
from newdial_ui import Ui_Dialog
from finddial import Ui_fDial
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtCore import QSize, QDate
from PySide6.QtGui import QColor
from PySide6.QtCore import QItemSelectionModel
#import PySide6.QtGui
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

        self.updateWidg("SELECT * FROM jtab;","SELECT COUNT(*) FROM jtab;")


        
    def updateWidg(self, que, quec):
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
            self.ui.tableWidget.setItem(r, 5,  QTableWidgetItem(str(query.value(5))))
            self.ui.tableWidget.setItem(r, 6,  QTableWidgetItem(str(query.value(6))))
            self.ui.tableWidget.setItem(r, 7,  QTableWidgetItem(str(query.value(8))))
            if str(query.value(7)) == "True":  # оплачено
                for c in range(self.ui.tableWidget.columnCount()):
                    self.ui.tableWidget.item(r, c).setBackground(QColor(0, 250, 100))  # Должно поменять цвет строки
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
        self.ui.tableWidget.resizeColumnToContents(5)
        self.ui.tableWidget.resizeColumnToContents(6)
      #  self.ui.tableWidget.setColumnWidth(7, 500)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)


    def findRec(self):
        fdlg=fnddial()
        fdlg.exec()
        #self.updateWidg("SELECT *  FROM jtab WHERE numZak = '3028' ;", "SELECT COUNT(*) FROM jtab WHERE numZak = '3028' ;")

        #pass

    def addRec(self):


        qcount = QSqlQuery()
        qcount.exec("SELECT MAX(npp) FROM jtab")
        qcount.first()
        dlg = newdial(self, int(qcount.value(0))+1,0)
        dlg.exec()


    def changeRec(self):
        #currow=self.ui.tableWidget.currentRow()

        dlg = newdial(self, self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text(),1)
        dlg.exec()

    def delRec(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Удаление записи")
        txtd = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text()
        dlg.setText("Уверены в удалении строки с номером заказа "+txtd+"?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            adq = QSqlQuery()
            adq.exec("DELETE FROM jtab WHERE npp = "+self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()+";")
            self.updateWidg("SELECT * FROM jtab;","SELECT COUNT(*) FROM jtab;")
        else:
            print("No!")

    def formUpd(self):
        pass
      #  jmod=QSqlTableModel()
      #  jmod.setTable("jtab")
      #  self.ui.tableView.setModel(jmod)
      #  jmod.select()

class newdial(QDialog):
    def __init__(self, parent=None, npp = 0,ceFlagp=0 ):
        global mainW, ceFlag
        ceFlag= ceFlagp
        mainW=parent
        super().__init__(parent)
        # Run the .setupUi() method to show the GUI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lineEdit_npp.setText(str(npp))
        self.ui.buttonBox.accepted.connect(self.okButton)
        self.ui.buttonBox.rejected.connect(self.rejButton)
        if ceFlag == 1:
            qinp = QSqlQuery()
            qinp.exec("SELECT * FROM jtab WHERE npp = "+str(npp)+" ;")
            qinp.first()
            self.ui.lineEdit_dat.setText(qinp.value(1))
            self.ui.lineEdit_numZak.setText(str(qinp.value(2)))
            self.ui.lineEdit_phone.setText(qinp.value(3))
            self.ui.lineEdit_nameZak.setText(qinp.value(4))
            self.ui.textEdit_descryption.setText(qinp.value(5))
            self.ui.lineEdit_costSum.setText(str(qinp.value(6)))
            self.ui.checkBox_costYN.setChecked(bool(qinp.value(7)))
            self.ui.textEdit_prim.setText(qinp.value(8))
        else:
            qdate = QDate.currentDate()
            sd = str(qdate.day())
            if len(sd) == 1:
                sd = "0" + sd
            sm = str(qdate.month())
            if len(sm) == 1:
                sm = "0" + sm
            stdate = sd + "." + sm + "." + str(qdate.year())
            self.ui.lineEdit_dat.setText(stdate)
            qnz = QSqlQuery()
            qnz.exec("SELECT MAX(numZak) FROM jtab")
            qnz.first()
            self.ui.lineEdit_numZak.setText(str(qnz.value(0)+1))

        
    def okButton(self):
        qinsert = QSqlQuery()
        if ceFlag == 0:
            inNewRow = "INSERT INTO jtab VALUES ("+self.ui.lineEdit_npp.text()+", '"+self.ui.lineEdit_dat.text()+"', "+self.ui.lineEdit_numZak.text()+", '"+self.ui.lineEdit_phone.text()+"', '"+self.ui.lineEdit_nameZak.text()+"', '"+self.ui.textEdit_descryption.toPlainText()+"', '"+self.ui.lineEdit_costSum.text()+"', "+str(self.ui.checkBox_costYN.isChecked())+", '"+self.ui.textEdit_prim.toPlainText()+"', "+str(self.ui.checkBox_end.isChecked())+");"
        if ceFlag == 1:
            inNewRow = "UPDATE jtab SET dat='"+self.ui.lineEdit_dat.text()+"', numzak= "+self.ui.lineEdit_numZak.text()+", phone='"+self.ui.lineEdit_phone.text()+"', nameZak= '"+self.ui.lineEdit_nameZak.text()+"', descryption='"+self.ui.textEdit_descryption.toPlainText()+"', costSum= "+self.ui.lineEdit_costSum.text()+", costYN= "+str(self.ui.checkBox_costYN.isChecked())+", prim= '"+self.ui.textEdit_prim.toPlainText()+"', End= "+str(self.ui.checkBox_end.isChecked())+" WHERE npp = "+self.ui.lineEdit_npp.text()+" ;"

        #print(inNewRow)
        qinsert.exec(inNewRow) 
        mainW.updateWidg("SELECT * FROM jtab;","SELECT COUNT(*) FROM jtab;")
        #mainW.hide()
        self.close()

    def rejButton(self):
        self.close()

class fnddial(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_fDial()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
