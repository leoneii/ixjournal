import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QMessageBox
from atolMain import Ui_MainWindow
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor
from PySide6.QtCore import QItemSelectionModel
from libfptr10 import IFptr


class MainWindow(QMainWindow):
    fptr = IFptr(r"/home/leone/app/atol10/linux-x64/")
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_USB))
    #fptr.setSingleSetting(IFptr.libLIBFPTR_SETTING_COM_FILE, "COM5")
    #fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
    fptr.showProperties(IFptr.LIBFPTR_GUI_PARENT_QT,None)
    fptr.applySingleSettings()
    fptr.open()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_test.clicked.connect(self.test)
        self.ui.closeShift.clicked.connect(self.closeShift)


    def closeShift(self):

        self.fptr.setParam(1021, "Кассир Иванов И.")
        self.fptr.setParam(1203, "123456789047")
        self.fptr.operatorLogin()

        self.fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_CLOSE_SHIFT)
        self.fptr.report()

        self.fptr.checkDocumentClosed()

    def test(self):


        ipAddress = self.fptr.getSingleSetting(IFptr.LIBFPTR_SETTING_IPADDRESS)
        ipPort = self.fptr.getSingleSetting(IFptr.LIBFPTR_SETTING_IPPORT)
        print(str(self.fptr.version())+" "+ipAddress+":"+ipPort)

        self.fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_MODEL_INFO)
        self.fptr.queryData()
        #model           = fptr.getParamInt(IFptr.LIBFPTR_PARAM_MODEL)
        #modelName       = fptr.getParamString(IFptr.LIBFPTR_PARAM_MODEL_NAME)
        #firmwareVersion = fptr.getParamString(IFptr.LIBFPTR_PARAM_UNIT_VERSION)
        print(str(self.fptr.getParamString(IFptr.LIBFPTR_PARAM_MODEL_NAME))+str(self.fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER)))
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