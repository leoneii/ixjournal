import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QMessageBox, QDialog
from main_ui import Ui_MainWindow
from newdial_ui import Ui_Dialog
from finddial import Ui_fDial
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtCore import QSize, QDate
from PySide6.QtGui import QColor
#from datetime import date
from PySide6.QtCore import QItemSelectionModel
#import PySide6.QtGui
#from PySide6 import QtWidgets

class MainWindow(QMainWindow):
    global Gcue, Gcuec,begd,stod
    Gcue="SELECT *  FROM jtab WHERE ZEND = False;"
    Gcuec="SELECT COUNT(*) FROM jtab WHERE ZEND = False ;"
    begd = QDate.fromString('01.01.2024','dd.MM.yyyy')
    stod = QDate.currentDate()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_Find.clicked.connect(self.findRec)
        self.ui.pushButton_UnFilter.clicked.connect(self.unFilter)
        self.ui.pushButton_Add.clicked.connect(self.addRec)
        self.ui.pushButton_Change.clicked.connect(self.changeRec)
        self.ui.tableWidget.doubleClicked.connect(self.changeRec)
        self.ui.pushButton_Del.clicked.connect(self.delRec)
        self.ui.pushButton_Ext.clicked.connect(self.Vidat)
        self.ui.pushButton_Pay.clicked.connect(self.Payed)

        # DB = QSqlDatabase.addDatabase('QIBASE')
        # DB.setDatabaseName("/home/leone/build/ixjournal/jourbd.fdb")
        # DB.setUserName("SYSDBA")
        # DB.setPassword("14062003")
        # DB.setConnectOptions("server type=Embedded; auto_commit=True;  auto_commit_level=4096; connection lifetime=1; DataBase= \":/home/leone/build/ixjournal/jourbd.fdb\"")
        # #DB.setHostName("embedded")

        DB = QSqlDatabase.addDatabase('QIBASE')
        DB.setHostName("192.168.1.59")
        DB.setPort(3050)
        DB.setDatabaseName("/srv/nfs4/DBS/ixjournal5.fdb")
        DB.setUserName("SYSDBA")
        DB.setPassword("14062003")
        DB.setConnectOptions( "auto_commit=True;  auto_commit_level=4096; connection lifetime=1;")

        DB.open()
        lastError = DB.lastError().text()
        print (lastError)
        #CREATE TABLE "jtab1"( "npp" INTEGER, "dat" TEXT, "numZak" INTEGER, "phone" TEXT, "nameZak" TEXT, "descryption" TEXT, "costSum" REAL, "costYN" BLOB, "prim" TEXT, "End" BLOB, PRIMARY KEY("npp" AUTOINCREMENT) );


        #self.updateWidg("SELECT * FROM jtab;","SELECT COUNT(*) FROM jtab;")
        self.updateWidg(Gcue, Gcuec)

    def message(self, title="ixJournal", msg=""):
        qmes=QMessageBox()
        qmes.setWindowTitle(title)
        qmes.setText(msg)    
        qmes.exec()

    def Payed(self):
        querv=QSqlQuery()
        querv.exec("UPDATE jtab SET costYN = 'True' WHERE  npp = "+self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()+" ;")
        self.message("ixJournal","Оплачено")
        self.updateWidg("LAST","")

    def Vidat(self):
        querv=QSqlQuery()
        querv.exec("UPDATE jtab SET zEND = 'True' WHERE  npp = "+self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()+" ;")
        self.message("ixJournal","Выдано")
        self.updateWidg("LAST","")

    def unFilter(self):
        global Gcue,Gcuec,begd,stod
        Gcue = "SELECT *  FROM jtab "
        Gcuec = "SELECT COUNT(*) FROM jtab ;"
        begd = '01.01.2024'
        now = QDate.currentDate()
        stod = now.toString('dd.MM.yyyy')
        self.updateWidg(Gcue,Gcuec)

    def updateWidg(self, que, quec):
        global Gcue,Gcuec;
        if que=='LAST':
            que=Gcue;
            quec=Gcuec;

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
            self.ui.tableWidget.setItem(r, 1,  QTableWidgetItem(QDate().fromString(query.value(1),'yyyy-MM-dd').toString('dd.MM.yyyy')))
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
        global Gcue,Gcuec,begd,stod
        fdlg=fnddial()#self.dateEditDATAInicial.setDate(QDate.currentDate())
        #now=QDate.currentDate()

        fdlg.ui.dateEdit_Start.setDate(begd)
        fdlg.ui.dateEdit_End.setDate(stod)
   

        def contUpdate(self,like=""):
            qcont = QSqlQuery()
            if like=="ALL":
                qcont.exec("SELECT name FROM jcont ;")
            else:
                qcont.exec("SELECT name FROM jcont WHERE name CONTAINING '"+fdlg.ui.comboBox_cont.currentText()+"';")  

            for ind in range(0,fdlg.ui.comboBox_cont.count()+1):
                fdlg.ui.comboBox_cont.removeItem(ind)  
        
            while (qcont.next()):
                fdlg.ui.comboBox_cont.addItem(qcont.value(0))

        contUpdate("ALL")
        fdlg.exec()

        dstart = fdlg.ui.dateEdit_Start.date()
        dstop = fdlg.ui.dateEdit_End.date()
        begd = dstart
        stod = dstop
        numz=fdlg.ui.lineEdit_numbZak.text()
        namez=fdlg.ui.comboBox_cont.currentText()
        # firstdat=QDate.strptime(dstart,'%d.%m.%Y')
        # secondat=QDate.strptime(dstop,'%d.%m.%Y')
        # print(firstdat)

        if len(numz)>0:
            self.updateWidg("SELECT *  FROM jtab WHERE numZak = '" + numz + "';" , "SELECT COUNT(*) FROM jtab WHERE numZak = '"+numz+"' ;")
            Gcue="SELECT *  FROM jtab WHERE numZak = '" + numz + "';"
            Gcuec="SELECT COUNT(*) FROM jtab WHERE numZak = '"+numz+"' ;"
        else:
            if len(namez)>0:
                upnamez=namez.upper()
                self.updateWidg("SELECT * FROM jtab WHERE (dat between '" + dstart.toString(
                    'yyyy-MM-dd') + "' and '" + dstop.toString('yyyy-MM-dd') + "') and nameZak CONTAINING  '"+namez+"';",
                                "SELECT COUNT(*) FROM jtab WHERE (dat between '" + dstart.toString(
                                    'yyyy-MM-dd') + "' and '" + dstop.toString('yyyy-MM-dd') + "')  and nameZak CONTAINING '"+namez+"';")

                Gcue = "SELECT * FROM jtab WHERE (dat between '" + dstart.toString('yyyy-MM-dd') + "' and '" + dstop.toString('yyyy-MM-dd') + "') and nameZak CONTAINING '"+namez+"';"
                Gcuec = "SELECT COUNT(*) FROM jtab WHERE (dat between '" + dstart.toString('yyyy-MM-dd') + "' and '" + dstop.toString('yyyy-MM-dd') + "')  and nameZak CONTAINING '"+namez+"';"
            else:
                self.updateWidg("SELECT * FROM jtab WHERE dat between '"+dstart.toString('yyyy-MM-dd')+"' and '"+dstop.toString('yyyy-MM-dd')+"';","SELECT COUNT(*) FROM jtab WHERE dat between '"+dstart.toString('yyyy-MM-dd')+"' and '"+dstop.toString('yyyy-MM-dd')+"';")
                Gcue ="SELECT * FROM jtab WHERE dat between '"+dstart.toString('yyyy-MM-dd')+"' and '"+dstop.toString('yyyy-MM-dd')+"';"
                Gcuec="SELECT COUNT(*) FROM jtab WHERE dat between '"+dstart.toString('yyyy-MM-dd')+"' and '"+dstop.toString('yyyy-MM-dd')+"';"
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
            self.updateWidg("LAST","")
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
       # self.ui.comboBox_cont .connect(self.contUpdate)
        self.ui.toolButton_phonFromTable.clicked.connect(self.phonFromTable)
        
        self.contUpdate("ALL")

        if ceFlag == 1:
            qinp = QSqlQuery()
            qinp.exec("SELECT * FROM jtab WHERE npp = "+str(npp)+" ;")
            qinp.first()
            self.ui.lineEdit_dat.setText(QDate().fromString(qinp.value(1),'yyyy-MM-dd').toString('dd.MM.yyyy'));
            self.ui.lineEdit_numZak.setText(str(qinp.value(2)))
            self.ui.lineEdit_phone.setText(qinp.value(3))
            self.ui.comboBox_cont.setCurrentText(qinp.value(4))
            self.ui.textEdit_descryption.setText(qinp.value(5))
            self.ui.lineEdit_costSum.setText(str(qinp.value(6)))
            self.ui.checkBox_costYN.setChecked(bool(qinp.value(7)))
            self.ui.textEdit_prim.setText(qinp.value(8))
            self.ui.checkBox_end.setChecked(bool(qinp.value(9)))
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
            self.ui.lineEdit_costSum.setText("0")

    def contUpdate(self,like=""):
        qcont = QSqlQuery()
        if like=="ALL":
            qcont.exec("SELECT name FROM jcont ;")
        else:
            qcont.exec("SELECT name FROM jcont WHERE name CONTAINING '"+self.ui.comboBox_cont.currentText()+"';")  

        for ind in range(0,self.ui.comboBox_cont.count()+1):
            self.ui.comboBox_cont.removeItem(ind)  
        
        while (qcont.next()):
            self.ui.comboBox_cont.addItem(qcont.value(0))

    def phonFromTable(self):
        qphone = QSqlQuery()
        qphone.exec("SELECT phone FROM JCONT WHERE NAME = '"+self.ui.comboBox_cont.currentText()+"';")
        qphone.first()
        self.ui.lineEdit_phone.setText(str(qphone.value(0)))

    def okButton(self):
        qinsert = QSqlQuery()
        dat = QDate().fromString(self.ui.lineEdit_dat.text(), 'dd.MM.yyyy').toString('yyyy-MM-dd');
        if ceFlag == 0:
            inNewRow = "INSERT INTO jtab VALUES ("+self.ui.lineEdit_npp.text()+", '"+dat+"', "+self.ui.lineEdit_numZak.text()+", '"+self.ui.lineEdit_phone.text()+"', '"+self.ui.comboBox_cont.currentText()+"', '"+self.ui.textEdit_descryption.toPlainText()+"', '"+self.ui.lineEdit_costSum.text()+"', '"+str(self.ui.checkBox_costYN.isChecked())+"', '"+self.ui.textEdit_prim.toPlainText()+"', '"+str(self.ui.checkBox_end.isChecked())+"');"
        if ceFlag == 1:
            inNewRow = "UPDATE jtab SET dat='"+dat+"', numzak= "+self.ui.lineEdit_numZak.text()+", phone='"+self.ui.lineEdit_phone.text()+"', nameZak= '"+self.ui.comboBox_cont.currentText()+"', descryption='"+self.ui.textEdit_descryption.toPlainText()+"', costSum= "+self.ui.lineEdit_costSum.text()+", costYN= '"+str(self.ui.checkBox_costYN.isChecked())+"', prim= '"+self.ui.textEdit_prim.toPlainText()+"', ZEND= '"+str(self.ui.checkBox_end.isChecked())+"' WHERE npp = "+self.ui.lineEdit_npp.text()+" ;"
            #print("UPDATE jtab SET dat='"+dat+"', numzak= "+self.ui.lineEdit_numZak.text()+", phone='"+self.ui.lineEdit_phone.text()+"', nameZak= '"+self.ui.lineEdit_nameZak.text()+"', descryption='"+self.ui.textEdit_descryption.toPlainText()+"', costSum= "+self.ui.lineEdit_costSum.text()+", costYN= '"+str(self.ui.checkBox_costYN.isChecked())+"', prim= '"+self.ui.textEdit_prim.toPlainText()+"', zEND= '"+str(self.ui.checkBox_end.isChecked())+"' WHERE npp = "+self.ui.lineEdit_npp.text()+" ;")
        qinsert.exec(inNewRow) 

        #CONT ОБНОВЛЯЕМ
        qcont = QSqlQuery()
        qcont.exec("SELECT COUNT(*) FROM JCONT WHERE NAME = '"+self.ui.comboBox_cont.currentText()+"';")
        qcont.first()
        #print(qcont.value(0))
        if int(qcont.value(0))==0:
            mbx = QMessageBox(QMessageBox.Warning,"ixJournal","Такого контрагента нет в справочнике, добавить?",QMessageBox.Save | QMessageBox.Discard ).exec()
            if mbx != QMessageBox.Discard :
                qcont.exec("INSERT INTO JCONT (name,phone) VALUES ('"+self.ui.comboBox_cont.currentText()+"','"+self.ui.lineEdit_phone.text()+"');")
        else:
            qcont.exec("UPDATE JCONT SET phone ='"+self.ui.lineEdit_phone.text()+"' WHERE NAME = '"+self.ui.comboBox_cont.currentText()+"';")

        mainW.updateWidg("LAST","")
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
