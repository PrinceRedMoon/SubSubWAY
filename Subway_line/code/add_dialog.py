from PyQt5.QtWidgets import QDialog
from PyQt5 import  QtWidgets
from code.add_ui import Ui_Dialog
from code import Subway_data as Subway_data


# from PyQt5.QtWidgets import QApplication

class add_dialog(QDialog,Ui_Dialog):
    def __init__(self):
        super(add_dialog,self).__init__()
        self.setupUi(self)
        self.ok.clicked.connect(self.ok_button)
        self.cancel.clicked.connect(self.close)
    def ok_button(self):
        station=self.s_input.text()
        adj=self.adj_input.text()
        weight=self.dis_input.text()
        line=self.line_input.text()
        x=self.x_input.text()
        y=self.y_input.text()
        label_x=self.labelx_input.text()
        label_y=self.labely_input.text()
        if station == "":
            QtWidgets.QMessageBox.question(self.Dialog, "Error!", "请输入添加站", QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            return
        elif adj not in Subway_data.subway_net.station_list.keys() and adj!= "":
            QtWidgets.QMessageBox.question(self.Dialog, "Error!", "请输入已有站点作为相邻站或者不填相邻站", QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            return
        elif (weight== "" and adj in Subway_data.subway_net.station_list.keys()) or (weight.isnumeric() is False and adj in Subway_data.subway_net.station_list.keys()):
            QtWidgets.QMessageBox.question(self.Dialog, "Error!", "距离信息错误，请重新输入距离信息", QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            return
        elif line== "":
            QtWidgets.QMessageBox.question(self.Dialog, "Error!", "请输入线路信息", QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            return
        elif x== "" or y== "" or label_x== "" or label_y== "" or x.isnumeric() is False or y.isnumeric() is False or label_x.isnumeric() is False or label_y.isnumeric() is False and adj=="":
            QtWidgets.QMessageBox.question(self.Dialog, "Error!", "站点坐标信息错误，请重新输入添加站坐标信息(已添加站点不会因此更改信息)", QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            return
        else:
            if station in Subway_data.subway_net.station_list.keys() :
                Subway_data.add_station(station, adj, weight, line, "NULL", "NULL", "NULL", "NULL")
            else:
                Subway_data.add_station(station, adj, weight, line, x, y, label_x, label_y)
        self.close()