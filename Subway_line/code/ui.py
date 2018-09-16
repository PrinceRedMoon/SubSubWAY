# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qt\subway.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
from code.add_dialog import add_dialog as ADDdialog
from code.delete_dialog import delete_dialog as DELETEdialog
import time
from code import algorithms as algorithms, Subway_data as Subway_data
import networkx as nx
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
plt.rcParams['font.sans-serif']=['SimHei']#设置中文

class Ui_SubSubWay(object):
    def setupUi(self, SubSubWay):
        self.SubSubWay=SubSubWay
        SubSubWay.setObjectName("SubSubWay")
        SubSubWay.resize(1200, 990)
        SubSubWay.setMinimumSize(QtCore.QSize(0, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubSubWay.setWindowIcon(icon)
        SubSubWay.setToolTipDuration(2)

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        SubSubWay.setFont(font)

        #窗口居中
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = SubSubWay.frameGeometry()
        SubSubWay.move((self.screen.width() - size.width()) / 2, 0)

        #背景白色
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        SubSubWay.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(SubSubWay)
        self.centralwidget.setObjectName("centralwidget")

        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 591, 54))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        #起始站输入
        self.inputstart = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.inputstart.setMinimumSize(QtCore.QSize(0, 50))
        self.inputstart.setObjectName("inputstart")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputstart)
        self.start = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.start.setMinimumSize(QtCore.QSize(0, 40))
        self.start.setObjectName("start")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.start)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.end = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.end.setMinimumSize(QtCore.QSize(0, 40))
        self.end.setObjectName("end")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.end)
        #终点站输入
        self.inputend = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.inputend.setMinimumSize(QtCore.QSize(0, 50))
        self.inputend.setObjectName("inputend")

        # 地图显示
        self.map = QtWidgets.QWidget(self.centralwidget)
        self.map.setGeometry(QtCore.QRect(100, 140, 1000, 700))  # 定义gridLayout控件的大小和位置，4个数字分别为左边坐标，上边坐标，长，宽
        self.map.setObjectName("map")
        self.map2 = QtWidgets.QGridLayout(self.map)
        self.map2.setObjectName("map2")
        # # ===通过graphicview来显示图形
        # self.graphicview = QtWidgets.QGraphicsView(self.map)  # 第一步，创建一个QGraphicsView，注意同样以gridLayoutWidget为参
        # self.graphicview.setObjectName("graphicview")
        # self.map2.addWidget(self.graphicview, 0, 0)

        self.m =d_map()
        self.m.normal()
        self.map2.addWidget(self.m.canvas)
        # graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        # graphicscene.addWidget(m.canvas)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        # self.graphicview.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        # self.graphicview.show()  # 最后，调用show方法呈现图形！Voila!!

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputend)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout_2)
        # 最少换乘按钮
        self.leastchange = QtWidgets.QPushButton(self.centralwidget)
        self.leastchange.setGeometry(QtCore.QRect(20, 70, 131, 41))
        self.leastchange.setObjectName("leastchange")
        self.leastchange.clicked.connect(self.map_change)
        # 最短距离按钮
        self.leastdistance = QtWidgets.QPushButton(self.centralwidget)
        self.leastdistance.setGeometry(QtCore.QRect(170, 70, 131, 41))
        self.leastdistance.setObjectName("leastdistance")
        self.leastdistance.clicked.connect(self.map_distance)
        # 确定按钮
        self.ensure = QtWidgets.QPushButton(self.centralwidget)
        self.ensure.setGeometry(QtCore.QRect(630, 10, 50, 50))
        self.ensure.setObjectName("ensure")
        self.ensure.clicked.connect(self.get_routine)
        #帮助按钮
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(1140, 10, 50, 50))
        self.help.setObjectName("help")
        self.help.clicked.connect(self.help_info)
        #添加站点按钮
        self.add_station = QtWidgets.QPushButton(self.centralwidget)
        self.add_station.setGeometry(QtCore.QRect(840, 10, 100, 50))
        self.add_station.setObjectName("add_station")
        self.add_station.clicked.connect(self.add_s)
        #删除站点按钮
        self.del_station = QtWidgets.QPushButton(self.centralwidget)
        self.del_station.setGeometry(QtCore.QRect(990, 10, 100, 50))
        self.del_station.setObjectName("del_station")
        self.del_station.clicked.connect(self.delete_s)

        # 其他路线显示
        self.elseroutine = QtWidgets.QTextBrowser(self.centralwidget)
        self.elseroutine.setGeometry(QtCore.QRect(100, 860, 1000, 120))
        self.elseroutine.setObjectName("elseroutine")

        SubSubWay.setCentralWidget(self.centralwidget)
        self.retranslateUi(SubSubWay)
        QtCore.QMetaObject.connectSlotsByName(SubSubWay)

    def retranslateUi(self, SubSubWay):
        _translate = QtCore.QCoreApplication.translate
        SubSubWay.setWindowTitle(_translate("SubSubWay", "SubSub WAY"))
        self.start.setText(_translate("SubSubWay", "<html><head/><body><p><span style=\" font-size:11pt;\">请输入起点：</span></p></body></html>"))
        self.end.setText(_translate("SubSubWay", "<html><head/><body><p><span style=\" font-size:11pt;\">请输入终点：</span></p></body></html>"))
        self.leastchange.setText(_translate("SubSubWay", "最少换乘路线"))
        self.leastchange.setToolTip("点击动态演示最少换乘路线")
        self.leastdistance.setText(_translate("SubSubWay", "最短距离路线"))
        self.leastdistance.setToolTip("点击动态演示最短距离路线")
        self.ensure.setText(_translate("SubSubWay", "√"))
        self.ensure.setToolTip("点击计算线路，请不要在动态演示时点击")
        self.help.setText(_translate("SubSubWay", "？"))
        self.help.setToolTip("点击获得帮助")
        self.add_station.setText(_translate("SubSubWay", "添加站点"))
        self.add_station.setToolTip("点击添加站点")
        self.del_station.setText(_translate("SubSubWay", "删除站点"))
        self.del_station.setToolTip("点击删除站点")

    def get_routine(self):
        self.m.normal()
        self.start = self.inputstart.text()
        self.end = self.inputend.text()
        if self.start not in Subway_data.subway_net.station_list.keys() or self.end not in Subway_data.subway_net.station_list.keys():
            QtWidgets.QMessageBox.question(self.SubSubWay,"Error!","请输入正确的站点名称",QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            return
        station_net= Subway_data.subway_net
        line_list={}
        Subway_data.create_linelist(station_net, line_list)
        self.shortestchange = algorithms.shortestchange_path(station_net, self.start, self.end, line_list)
        self.shortestdistance= algorithms.shortestdistance_path(station_net, self.start, self.end, 0)
        self.otherOne= algorithms.otherONE_path(station_net, self.start, self.end)
        self.otherTwo= algorithms.otherTWO_path(station_net, self.start, self.end)
        self.otherThree= algorithms.otherTHREE_path(station_net, self.start, self.end)
        #整合字符串，有重复线路不重复显示
        count = 1
        self.routine=str(count)+"、" + '→'.join(self.otherOne[:-3])+ "\n"
        if self.otherOne[:-3]!=self.otherTwo[:-1]:
            count=count+1
            self.routine=self.routine+str(count)+"、" + '→'.join(self.otherTwo[:-1]) + "\n"
        if self.otherThree[-1] == 1:
            if self.otherOne[:-3] != self.otherThree[:-1] and self.otherTwo[:-1] != self.otherThree[:-1]:
                count=count+1
                self.routine = self.routine + str(count)+"、" + '→'.join(self.otherThree[:-1]) + "\n"
        else:
             self.otherThree.pop(0)
             for path in self.otherThree:
                if self.otherOne[:-3] != path[:-3] and self.otherTwo[:-1] != path[:-3]:
                    count = count + 1
                    self.routine = self.routine + str(count) + "、" + '→'.join(path[:-3]) + "\n"
        #将text添加到textbrowser输出
        self.elseroutine.setText("路线：\n"+self.routine)

    def map_distance(self):
        self.m.normal()
        if self.start not in Subway_data.subway_net.station_list.keys() or self.end not in Subway_data.subway_net.station_list.keys():
            QtWidgets.QMessageBox.question(self.SubSubWay,"Error!","请输入正确的站点名称并点击√进行计算",QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            return
        for station in self.shortestdistance[:-1]:
            list=[station]
            self.m.short(list)
            QtWidgets.QApplication.processEvents()#该函数的作用是让程序处理那些还没有处理的事件，然后再把使用权返回给调用者。
            time.sleep(0.3)

    def map_change(self):
        self.m.normal()
        if self.start not in Subway_data.subway_net.station_list.keys() or self.end not in Subway_data.subway_net.station_list.keys():
            QtWidgets.QMessageBox.question(self.SubSubWay,"Error!","请输入正确的站点名称并点击√进行计算",QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            return
        for station in self.shortestchange[:-1]:
            list=[station]
            self.m.short(list)
            QtWidgets.QApplication.processEvents()
            time.sleep(0.3)

    def add_s(self):
        A=ADDdialog()
        A.show()
        A.exec_()
        self.m.normal()

    def delete_s(self):
        A = DELETEdialog()
        A.show()
        A.exec_()
        self.m.normal()

    def help_info(self):
        QtWidgets.QMessageBox.information(self.SubSubWay, "帮助","添加站点：\n\t1、可添加单独站点。(相邻站和距离默认为无)\n\t"
                                                            "2、可添加边。(相邻站必须为已有站点)\n\t"
                                                            "3、坐标均为添加站点坐标。\n\t4、只有个别线路有指定颜色，其他线路颜色默认。\n\t"
                                                            "5、线路需填写中文线路名称。(如四号线)\n"
                                                            "删除站点：\n\t1、可删除所有站点。(固有站点在下一次重新开启程序时恢复，但添加站点不会)\n"
                                                            "注意！！动态演示时请勿进行任何操作！\n"
                                                            "如需再次帮助，请点击右上角图标！", QtWidgets.QMessageBox.Ok,)

class d_map:
    def __init__(self):
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
    def normal(self):   #初始地图
        self.figure.clf()

        self.station_net = Subway_data.subway_net
        self.position = Subway_data.pos
        self.position_label = Subway_data.pos_label
        # 初始化color表
        self.N_COLOR = []
        self.E_COLOR = []
        e_visited = []
        # 创建图
        self.G = nx.Graph()
        for station in self.station_net.station_list.keys():
            self.N_COLOR.append("w")
            self.G.add_node(station)
        for station in self.station_net.station_list.keys():
            for adj in self.station_net.station_list[station].get_neighbor():
                self.G.add_edge(station, adj)
                # 防止重复边颜色
                if (station, adj) not in e_visited:
                    if self.station_net.station_list[station].adj[adj][-1] == "一号线":
                        self.E_COLOR.append("#C33A30")
                    elif self.station_net.station_list[station].adj[adj][-1] == "二号线":
                        self.E_COLOR.append("#016098")
                    elif self.station_net.station_list[station].adj[adj][-1] == "五号线":
                        self.E_COLOR.append("#A62081")
                    elif self.station_net.station_list[station].adj[adj][-1] == "六号线":
                        self.E_COLOR.append("#D29600")
                    elif self.station_net.station_list[station].adj[adj][-1] == "十号线":
                        self.E_COLOR.append("#019BC1")
                    elif self.station_net.station_list[station].adj[adj][-1] == "四号线":
                        self.E_COLOR.append("#008E9C")
                    elif self.station_net.station_list[station].adj[adj][-1] == "七号线":
                        self.E_COLOR.append("#FAC672")
                    elif self.station_net.station_list[station].adj[adj][-1] == "八号线":
                        self.E_COLOR.append("#019A6B")
                    elif self.station_net.station_list[station].adj[adj][-1] == "九号线":
                        self.E_COLOR.append("#8FC320")
                    elif self.station_net.station_list[station].adj[adj][-1] == "十三号线":
                        self.E_COLOR.append("#F9E701")
                    elif self.station_net.station_list[station].adj[adj][-1] == "十四号线":
                        self.E_COLOR.append("#D6A7A1")
                    elif self.station_net.station_list[station].adj[adj][-1] == "十五号线":
                        self.E_COLOR.append("#5C2C68")
                    else:
                        self.E_COLOR.append("k")
                # 将已添加的无向边加入list
                e_visited.append((station, adj))
                e_visited.append((adj, station))
        # 画没有标签图
        nx.draw(self.G, pos=self.position, node_size=60, width=3.0, with_labels=False, node_color=self.N_COLOR, edge_color=self.E_COLOR)
        # 添加节点outline
        ax = plt.gca()
        ax.collections[0].set_edgecolor("#C0C0C0")
        # 画标签
        nx.draw_networkx_labels(self.G, pos=self.position_label, font_size=9)
        self.canvas.draw_idle()
    def short(self,list):
        a=0
        for station in self.station_net.station_list.keys():
            if station in list:
                self.N_COLOR[a] = "#00FF00"
                break
            a = a + 1
        nx.draw_networkx_nodes(self.G, pos=self.position, node_size=50, node_color=self.N_COLOR)
        # 添加节点outline
        ax = plt.gca()
        ax.collections[0].set_edgecolor("#C0C0C0")
        self.canvas.draw()

import code.icon_rc
