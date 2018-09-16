# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qt\delete.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog=Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.setModal(True)
        Dialog.resize(300, 200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setToolTipDuration(2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        Dialog.setFont(font)

        # 窗口居中
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = Dialog.frameGeometry()
        Dialog.move((self.screen.width() - size.width()) / 2, 0)

        # 背景白色
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
        Dialog.setPalette(palette)

        self.del_label = QtWidgets.QLabel(Dialog)
        self.del_label.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.del_label.setObjectName("del_label")
        self.del_input = QtWidgets.QLineEdit(Dialog)
        self.del_input.setGeometry(QtCore.QRect(50, 70, 191, 41))
        self.del_input.setObjectName("del_input")
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(40, 150, 93, 28))
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(170, 150, 93, 28))
        self.cancel.setObjectName("cancel")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "删除站点"))
        self.ok.setText(_translate("Dialog", "OK"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.del_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">请输入要删除的站点：</span></p></body></html>"))

