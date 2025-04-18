import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QMessageBox, QDialog, QStyle, QMenu
from main_ui import Ui_MainWindow
from newdial_ui import Ui_Dialog
from finddial import Ui_fDial
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtCore import QSize, QDate
from PySide6.QtGui import QColor, QValidator, QDoubleValidator, Qt , QAction, QIcon, QKeyEvent
from PySide6.QtCore import QItemSelectionModel
#import PySide6.QtGui
#from PySide6 import QtWidgets
from costSum_ui import Ui_costSum
from sprav_ui import Ui_spDialog
import urllib
import json
import urllib.request
import urllib.parse
import os; 
import locale;
from QSearch_ui import Ui_Dialog_QSearch

import cascade_idigital

os.environ["PYTHONIOENCODING"] = "utf-8"; 
myLocale=locale.setlocale(category=locale.LC_ALL, locale="ru_RU.UTF-8");


#вот где можно прописывать всякие функции типа QMessagebox))
def toFixed(f: float, n=0):
    a, b = str(f).split('.')
    return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))

def message( parent = None, title="ixJournal", msg="" ):
    qmes=QMessageBox(parent)
   # qmes.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter, qmes.size(), qmes.geometry()));
    qmes.setWindowTitle(title)
    qmes.setText(msg)    
    qmes.setModal(True)
    qmes.setIcon(QMessageBox.Icon.Information)
    qmes.exec()

def backupToFile(parent = None, file = "backup.sql"):
    qbf = QSqlQuery()
    qbf.exec("OUTPUT "+file+";"
             "SELECT * FROM jtab;"
             "OUTPUT;") 
    

# Отправка SMS на чистом Python через sms-шлюз SMSPILOT.RU подготовка

def sendSMS( parent= None, type = 'NUM', phoneOrRow= '0', Query = True, text = 'Ваш заказ готов, Инфоникс Фатеж Пн-Пт 10-17,Сб 10-15 Сумма:',Sum = 0):

    

    if type =='NUM':
        phone = phoneOrRow
        Sum = 0
        prim = ""
        Row = '0'
    else:
        qinp = QSqlQuery()
        qinp.exec("SELECT phone, costSum, prim FROM jtab WHERE npp = "+phoneOrRow+" ;")
        qinp.first()
        phone = str(qinp.value(0))
        Sum = int(qinp.value(1))
        prim = str(qinp.value(2)) 
        Row = phoneOrRow

    if Sum != 0:
        text = text + " "+str(Sum)+"руб." 
        textMessager = "Ваш заказ готов к выдаче, Инфоникс Фатеж Пн-Пт 10-17,Сб 10-15 Сумма:"+ " "+str(Sum)+"руб." 
    else:
        textMessager = "Ваш заказ готов к выдаче, Инфоникс Фатеж Пн-Пт 10-17,Сб 10-15 Сумма:0 руб."     

    if Query == True:
        mbq = QMessageBox(QMessageBox.Warning,"ixJournal","Отправить сообщение клиенту?",QMessageBox.Ok | QMessageBox.Discard, parent ).exec()
        if mbq != QMessageBox.Discard :
            senderSMS(parent, phone,text,textMessager,prim,Row)
    else:
        senderSMS(parent, phone,text,textMessager,prim,Row)



# Функция непосредственной отправки смс
def senderSMS(parent= None, phone= None, text= None,textMessager= None, prim= "",Row ='0' ):
    #sender = 'NFXnet' #  имя отправителя из списка https://smspilot.ru/my-sender.php

    j = cascade_idigital.cascade(None,phone,text,textMessager)

    # sender = 'INFORM'
    # apikey = 'C0C37F90PPSX2QAK8YBSYPPGE8X233741OSB2O306KTSP4TYJCT7VW07828607C7'
    # formatapi='json'

    # url = "http://smspilot.ru/api.php?"
    # params = urllib.parse.urlencode({'send':text, 'to':phone, 'from':sender, 'apikey':apikey, 'format':formatapi })
    # url=url+params

    # j = json.loads(urllib.request.urlopen(url.replace(" ", "%20")).read())

    

    
    if ('error' in j):
        message(parent,"Ошибка","СМС не отправлено " + str(j))
        return ('Ошибка: %s' % j)
    else:
        if Row!='0':
            qinp = QSqlQuery()
            qinp.exec("UPDATE jtab SET prim = '"+prim+" Сообщение успешно отправлено "+str(QDate.currentDate().toString('dd.MM.yyyy'))+"' WHERE npp = "+Row+" ;")
            #print("UPDATE jtab SET prim = '"+prim+" Смс успешно отправлена "+str(QDate.currentDate().toString('dd.MM.yyyy'))+"' WHERE npp = "+Row+" ;")
            qinp.first()
        return (j)




class MainWindow(QMainWindow):
    global Gcue, Gcuec,begd,stod
    Gcue="SELECT *  FROM jtab WHERE ZEND = False ORDER BY npp;"
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
        self.ui.pushButton_UnFilter_All.clicked.connect(self.unFilterAll)
        self.ui.pushButton_Exit.clicked.connect(self.close)
        self.ui.pushButton_WorkEnd.clicked.connect(self.WorkEnd)
        self.ui.pushButton_Renew.clicked.connect(self.Renew)
        self.ui.pushButton_Sprav.clicked.connect(self.spravScreen)
        self.ui.pushButton_notPay.clicked.connect(self.notPayedFilter)

    #Контекстное меню
        self.ui.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidget.customContextMenuRequested.connect(self.contextMenu)
    #быстрый поиск
        self.ui.tableWidget.horizontalHeader().sectionClicked.connect(self.startQSearch)

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

        #self.updateWidg("SELECT * FROM jtab;",зш"SELECT COUNT(*) FROM jtab;")
        self.updateWidg(Gcue, Gcuec)

    def startQSearch(self, i):
        column_text = self.ui.tableWidget.horizontalHeaderItem(i).text()
        if i == 2 or i == 3:
            QSearchdlg=QSearch(self,i, column_text)
            QSearchdlg.exec()

    def spravScreen(self):
        sprs=sprScr()
        sprs.exec()
        
    def contextMenu(self, pos):
         context = QMenu(self)
         actWorkEnd = QAction(QIcon("image/EndWork.png"),"Готов к выдаче",self)
         actPayed = QAction(QIcon("image/Payed.png"),"Отметить оплаченным",self)
         actExt = QAction(QIcon("image/Moved.png"),"Выдать клиенту",self)
         actDel = QAction(QIcon("image/remove.png"),"Удалить заказ",self)

         context.addAction(actWorkEnd)
         context.addAction(actPayed)
         context.addAction(actExt)
         context.addSeparator()
         context.addAction(actDel)

         actExt.triggered.connect(self.Vidat)
         actPayed.triggered.connect(self.Payed)
         actWorkEnd.triggered.connect(self.WorkEnd)
         actDel.triggered.connect(self.delRec)

         context.exec(self.mapToGlobal(pos))   

    def Renew(self):
        self.updateWidg("LAST","")

    def Payed(self):
        querv=QSqlQuery()
        querv.exec("UPDATE jtab SET costYN = 'True' WHERE  npp = "+self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()+" ;")
        message(self,"ixJournal","Оплачено")
        self.updateWidg("LAST","")

    def Vidat(self):
        querv=QSqlQuery()
        querv.exec("SELECT workend  FROM jtab WHERE npp = "+self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()+" ;")
        querv.first()
        if querv.value(0)==True:
            querv.exec("UPDATE jtab SET zEND = 'True' WHERE  npp = "+self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()+" ;")
            mbq = QMessageBox(QMessageBox.Warning,"ixJournal","Оплата от клиента получена?",QMessageBox.Ok | QMessageBox.Cancel, self ).exec()
            if mbq != QMessageBox.Cancel :
                self.Payed()
            message(self,"ixJournal","Выдано")
            self.updateWidg("LAST","")
        else:
            message(self,"ixJournal","Работы не завершены- необходимо отметить выполнение работы и проставить ее стоимость")


    def WorkEnd(self):
        querv=QSqlQuery()
        querv.exec("SELECT workend  FROM jtab WHERE npp = "+self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()+" ;")
        querv.first()
        if querv.value(0)==True:
            message(self,"ixJournal","Работы по этому заказу уже были завершены")
        else:    
            dlg = costSum(self,self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text())
            dlg.exec()
            
            sendSMS(self,'ROW',self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text())
            self.updateWidg("LAST","")

    def unFilter(self):
        global Gcue,Gcuec,begd,stod
        Gcue = "SELECT *  FROM jtab WHERE ZEND = False ORDER BY npp"
        Gcuec = "SELECT COUNT(*) FROM jtab WHERE ZEND = False ;"
        begd = QDate.fromString('01.01.2024','dd.MM.yyyy')
        stod = QDate.currentDate()
        self.updateWidg(Gcue,Gcuec)

    def notPayedFilter(self):
        global Gcue,Gcuec,begd,stod
        Gcue = "SELECT *  FROM jtab WHERE ZEND = True AND CostYN = False AND WorkEnd = True ORDER BY npp ;"
        Gcuec = "SELECT COUNT(*) FROM jtab WHERE ZEND = True AND CostYN = False AND WorkEnd = True ;"
        begd = QDate.fromString('01.01.2024','dd.MM.yyyy')
        stod = QDate.currentDate()
        self.updateWidg(Gcue,Gcuec)


    def unFilterAll(self):
        global Gcue,Gcuec,begd,stod
        Gcue = "SELECT *  FROM jtab ORDER BY npp "
        Gcuec = "SELECT COUNT(*) FROM jtab ;"
        begd = QDate.fromString('01.01.2024','dd.MM.yyyy')
        stod = QDate.currentDate()
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
            self.ui.tableWidget.setItem(r, 6,  QTableWidgetItem(toFixed(float(query.value(6)),2)))
            self.ui.tableWidget.setItem(r, 7,  QTableWidgetItem(str(query.value(8))))
            if str(query.value(10)) == "True":  # готовы
                for c in range(self.ui.tableWidget.columnCount()):
                    self.ui.tableWidget.item(r, c).setBackground(QColor(0, 180, 100))  # Должно поменять цвет строк
                if  str(query.value(9)) == 'True': # выданы
                    for c2 in range(self.ui.tableWidget.columnCount()):
                        self.ui.tableWidget.item(r, c2).setBackground(QColor(0, 128, 255))  # Должно поменять цвет строк
                    if  str(query.value(7)) == 'False': # НЕ оплачены
                        for c2 in range(self.ui.tableWidget.columnCount()):
                            self.ui.tableWidget.item(r, c2).setBackground(QColor(255, 128, 0))  # Должно поменять цвет строк
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
            self.updateWidg("SELECT *  FROM jtab WHERE numZak = '" + numz + "' ORDER BY npp;" , "SELECT COUNT(*) FROM jtab WHERE numZak = '"+numz+"' ;")
            Gcue="SELECT *  FROM jtab WHERE numZak = '" + numz + "' ORDER BY npp;"
            Gcuec="SELECT COUNT(*) FROM jtab WHERE numZak = '"+numz+"' ;"
        else:
            if len(namez)>0:
                self.updateWidg("SELECT * FROM jtab WHERE (dat between '" + dstart.toString(
                    'yyyy-MM-dd') + "' and '" + dstop.toString('yyyy-MM-dd') + "') and nameZak CONTAINING  '"+namez+"' ORDER BY npp ;",
                      "SELECT COUNT(*) FROM jtab WHERE (dat between '" + dstart.toString(
                                    'yyyy-MM-dd') + "' and '" + dstop.toString('yyyy-MM-dd') + "')  and nameZak CONTAINING '"+namez+"';")

                Gcue = "SELECT * FROM jtab WHERE (dat between '" + dstart.toString('yyyy-MM-dd') + "' and '" + dstop.toString('yyyy-MM-dd') + "') and nameZak CONTAINING '"+namez+"' ORDER BY npp;"
                Gcuec = "SELECT COUNT(*) FROM jtab WHERE (dat between '" + dstart.toString('yyyy-MM-dd') + "' and '" + dstop.toString('yyyy-MM-dd') + "')  and nameZak CONTAINING '"+namez+"';"
            else:
                self.updateWidg("SELECT * FROM jtab WHERE dat between '"+dstart.toString('yyyy-MM-dd')+"' and '"+dstop.toString('yyyy-MM-dd')+"';","SELECT COUNT(*) FROM jtab WHERE dat between '"+dstart.toString('yyyy-MM-dd')+"' and '"+dstop.toString('yyyy-MM-dd')+"' ORDER BY npp;")
                Gcue ="SELECT * FROM jtab WHERE dat between '"+dstart.toString('yyyy-MM-dd')+"' and '"+dstop.toString('yyyy-MM-dd')+"' ORDER BY npp;"
                Gcuec="SELECT COUNT(*) FROM jtab WHERE dat between '"+dstart.toString('yyyy-MM-dd')+"' and '"+dstop.toString('yyyy-MM-dd')+"';"

    def addRec(self):
        self.Renew()
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

class fnddial(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_fDial()
        self.ui.setupUi(self)


class sprScr(QDialog):
    def __init__(self, parent = None):
        super().__init__()
        self.ui = Ui_spDialog()
        self.ui.setupUi(self)
        self.ui.pushButton_zakaz.clicked.connect(self.czak)
        self.setParent(parent)

        qspr=QSqlQuery()
        countspr=QSqlQuery()
        countspr.exec("SELECT COUNT(*) FROM jcont ;")
        countspr.first()
        self.ui.tableWidget.setRowCount(int(countspr.value(0)))
        r=0
        while qspr.next():
            self.ui.tableWidget.setItem(r, 0,  QTableWidgetItem(str(qspr.value(0))))
            # self.ui.tableWidget.setItem(r, 0,  QTableWidgetItem(str(qspr.value(0))))
            # self.ui.tableWidget.setItem(r, 1,  QTableWidgetItem(str(qspr.value(1))))
            # self.ui.tableWidget.setItem(r, 2,  QTableWidgetItem(str(qspr.value(2))))
            # self.ui.tableWidget.setItem(r, 3,  QTableWidgetItem(str(qspr.value(3))))
            # self.ui.tableWidget.setItem(r, 4,  QTableWidgetItem(str(qspr.value(4))))
            # self.ui.tableWidget.setItem(r, 5,  QTableWidgetItem(str(qspr.value(5))))
            # self.ui.tableWidget.setItem(r, 6,  QTableWidgetItem(str(qspr.value(6))))
           
            r+=1          

    def czak(self):
        self.ui.label_selSprav.setText("Заказчик")


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
        self.ui.toolButton_phonFromTable.clicked.connect(self.phoneFromTable)
        self.ui.toolButton_textFrom1.clicked.connect(self.textFrom1)
        self.ui.toolButton_textFrom2.clicked.connect(self.textFrom2)
        self.ui.toolButton_textFrom3.clicked.connect(self.textFrom3)
        self.ui.toolButton_textFrom4.clicked.connect(self.textFrom4)
        self.ui.toolButton_textFrom5.clicked.connect(self.textFrom5)
        self.ui.toolButton_textFrom6.clicked.connect(self.textFrom6)
        self.ui.toolButton_textFrom7.clicked.connect(self.textFrom7)
        self.ui.lineEdit_clientCash.textChanged.connect(self.calcCash)
        self.ui.checkBox_WorkEnd.clicked.connect(self.workEndChange)
        self.ui.checkBox_end.clicked.connect(self.endChange)
        

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
            self.ui.lineEdit_costSum.setText(toFixed(float(qinp.value(6)),2))
            self.ui.checkBox_costYN.setChecked(bool(qinp.value(7)))
            self.ui.textEdit_prim.setText(qinp.value(8))
            self.ui.checkBox_end.setChecked(bool(qinp.value(9)))
            self.ui.checkBox_WorkEnd.setChecked(bool(qinp.value(10)))
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


    def workEndChange(self):
        if self.ui.checkBox_WorkEnd.isChecked():
            self.okButton(False)
            sendSMS(self,'ROW',self.ui.lineEdit_npp.text())
            qinp = QSqlQuery()
            qinp.exec("SELECT prim FROM jtab WHERE npp = "+self.ui.lineEdit_npp.text()+" ;")
            qinp.first()
            self.ui.textEdit_prim.setText(qinp.value(0))



    def endChange(self):
        if self.ui.checkBox_WorkEnd.isChecked()==False:
            message(self,"ixJournal","Работы еще не были завершены, нельзя выдать незавершенный заказ ")
            self.ui.checkBox_end.setChecked(False)
        if self.ui.checkBox_end.isChecked() and self.ui.checkBox_costYN.isChecked()==False:
            mbq = QMessageBox(QMessageBox.Warning,"ixJournal","Оплата от клиента получена?",QMessageBox.Ok | QMessageBox.Cancel, self ).exec()
            if mbq != QMessageBox.Cancel :
                self.ui.checkBox_costYN.setChecked(True)

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

    def textFrom1(self):
        self.ui.textEdit_descryption.insertPlainText("Заправка картриджа ")

    def textFrom2(self):
        self.ui.textEdit_descryption.insertPlainText("Не включается ")

    def textFrom3(self):
        self.ui.textEdit_descryption.insertPlainText("Не загружается в операционную систему ")       

    def textFrom4(self):
        self.ui.textEdit_descryption.insertPlainText(" + Блок питания  ")

    def textFrom5(self):
        self.ui.textEdit_descryption.insertPlainText("Ноутбук ")

    def textFrom6(self):
        self.ui.textEdit_descryption.insertPlainText("+ сумка ")       

    def textFrom7(self):
        self.ui.textEdit_descryption.insertPlainText(" Принтер, не работает ")

    def phoneFromTable(self):
        qphone = QSqlQuery()
        qphone.exec("SELECT phone FROM JCONT WHERE NAME = '"+self.ui.comboBox_cont.currentText()+"';")
        qphone.first()
        self.ui.lineEdit_phone.setText(str(qphone.value(0)))

    def okButton(self,close = True):
        qinsert = QSqlQuery()
        dat = QDate().fromString(self.ui.lineEdit_dat.text(), 'dd.MM.yyyy').toString('yyyy-MM-dd');
        if ceFlag == 0:
            inNewRow = "INSERT INTO jtab VALUES ("+self.ui.lineEdit_npp.text()+", '"+dat+"', "+self.ui.lineEdit_numZak.text()+", '"+self.ui.lineEdit_phone.text()+"', '"+self.ui.comboBox_cont.currentText()+"', '"+self.ui.textEdit_descryption.toPlainText()+"', '"+self.ui.lineEdit_costSum.text()+"', '"+str(self.ui.checkBox_costYN.isChecked())+"', '"+self.ui.textEdit_prim.toPlainText()+"', '"+str(self.ui.checkBox_end.isChecked())+"', '"+str(self.ui.checkBox_WorkEnd.isChecked())+"');"
        if ceFlag == 1:
            inNewRow = "UPDATE jtab SET dat='"+dat+"', numzak= "+self.ui.lineEdit_numZak.text()+", phone='"+self.ui.lineEdit_phone.text()+"', nameZak= '"+self.ui.comboBox_cont.currentText()+"', descryption='"+self.ui.textEdit_descryption.toPlainText()+"', costSum= "+self.ui.lineEdit_costSum.text()+", costYN= '"+str(self.ui.checkBox_costYN.isChecked())+"', prim= '"+self.ui.textEdit_prim.toPlainText()+"', ZEND= '"+str(self.ui.checkBox_end.isChecked())+"', workend= '"+str(self.ui.checkBox_WorkEnd.isChecked())+"' WHERE npp = "+self.ui.lineEdit_npp.text()+" ;"
            #print("UPDATE jtab SET dat='"+dat+"', numzak= "+self.ui.lineEdit_numZak.text()+", phone='"+self.ui.lineEdit_phone.text()+"', nameZak= '"+self.ui.lineEdit_nameZak.text()+"', descryption='"+self.ui.textEdit_descryption.toPlainText()+"', costSum= "+self.ui.lineEdit_costSum.text()+", costYN= '"+str(self.ui.checkBox_costYN.isChecked())+"', prim= '"+self.ui.textEdit_prim.toPlainText()+"', zEND= '"+str(self.ui.checkBox_end.isChecked())+"' WHERE npp = "+self.ui.lineEdit_npp.text()+" ;")
        qinsert.exec(inNewRow) 
        #
        #CONT ОБНОВЛЯЕМ
        qcont = QSqlQuery()
        qcont.exec("SELECT COUNT(*) FROM JCONT WHERE NAME = '"+self.ui.comboBox_cont.currentText()+"';")
        qcont.first()
        #print(qcont.value(0))
        if int(qcont.value(0))==0:
            mbx = QMessageBox(QMessageBox.Warning,"ixJournal","Такого контрагента нет в справочнике, добавить?",QMessageBox.Save | QMessageBox.Discard, self ).exec()
            
            if mbx != QMessageBox.Discard :
                qcont.exec("INSERT INTO JCONT (name,phone) VALUES ('"+self.ui.comboBox_cont.currentText()+"','"+self.ui.lineEdit_phone.text()+"');")
        else:
            qcont.exec("UPDATE JCONT SET phone ='"+self.ui.lineEdit_phone.text()+"' WHERE NAME = '"+self.ui.comboBox_cont.currentText()+"';")

        mainW.updateWidg("LAST","")
        if close==True:
            self.close()



    def rejButton(self):
        self.close()

    def calcCash(self):
        self.ui.lineEdit_clientRefund.setText(toFixed(float(self.ui.lineEdit_clientCash.text())-float(self.ui.lineEdit_costSum.text()),2))


class costSum(QDialog):
    def __init__(self, parent=None, Npp = '0' ):
        global npp
        npp=Npp
        super().__init__(parent)
        self.ui = Ui_costSum()
        self.ui.setupUi(self)
        self.ui.commandLinkButton_endWork.clicked.connect(self.WorkEnd)
        #self.ui.lineEdit_costSum.setValidator(QDoubleValidator(0.0, 999999.0, 2 ))
        qsum = QSqlQuery()
        qsum.exec("SELECT costSum FROM jtab WHERE npp='"+npp+"';")
        qsum.first()
        self.ui.lineEdit_costSum.setText(toFixed(float(qsum.value(0)),2))

    def WorkEnd(self):
        querv=QSqlQuery()
        querv.exec("UPDATE jtab SET workend = 'True', costSum='"+self.ui.lineEdit_costSum.text()+"' WHERE  npp = "+npp+" ;")
        message(self,"ixJournal","Работы над заказом завершены")
        self.close()

class QSearch(QDialog):
    def __init__(self, parent, column = 0, column_text="" ):
        #global par
        self.par=parent
        self.col=column
        super().__init__(parent)
        self.ui = Ui_Dialog_QSearch()
        self.ui.setupUi(self)
        self.setWindowTitle("Поиск по "+column_text)
        self.ui.toolButton_Filter.clicked.connect(self.Search)
        self.ui.toolButton_Cancel.clicked.connect(self.close)
        self.ui.comboBox.lineEdit().returnPressed.connect(self.Search)

    def Search(self):
        #global Gcue,Gcuec
        if self.col == 2:
            self.par.updateWidg("SELECT *  FROM jtab WHERE numZak CONTAINING '" + self.ui.comboBox.currentText() + "' ORDER BY npp;" , "SELECT COUNT(*) FROM jtab WHERE numZak CONTAINING '"+self.ui.comboBox.currentText() +"' ;")
        if self.col == 3:
            self.par.updateWidg("SELECT *  FROM jtab WHERE phone CONTAINING '" + self.ui.comboBox.currentText() + "' AND costYN = 'False' ORDER BY npp;" , "SELECT COUNT(*) FROM jtab WHERE phone CONTAINING '"+self.ui.comboBox.currentText() +"' AND costYN = 'False' ;")


        self.close()
           # Gcue="SELECT *  FROM jtab WHERE numZak = '" + numz + "' ORDER BY npp;"
           # Gcuec="SELECT COUNT(*) FROM jtab WHERE numZak = '"+numz+"' ;"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
