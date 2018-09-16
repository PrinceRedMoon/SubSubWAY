from PyQt5.QtWidgets import QDialog
from PyQt5 import  QtWidgets
from code.delete_ui import Ui_Dialog
from code import Subway_data as Subway_data


# from PyQt5.QtWidgets import QApplication

class delete_dialog(QDialog,Ui_Dialog):
    def __init__(self):
        super(delete_dialog,self).__init__()
        self.setupUi(self)
        self.ok.clicked.connect(self.ok_button)
        self.cancel.clicked.connect(self.close)
    def ok_button(self):
        station=self.del_input.text()
        if station not in Subway_data.subway_net.station_list.keys() :
            QtWidgets.QMessageBox.question(self.Dialog,"Error!","请删除正确的添加站！",QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            return
        Subway_data.delete_station(station)
        self.close()