# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToolUpSP.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ToolUPSP(object):
    def setupUi(self, ToolUPSP):
        ToolUPSP.setObjectName("ToolUPSP")
        ToolUPSP.resize(806, 407)
        font = QtGui.QFont()
        font.setPointSize(13)
        ToolUPSP.setFont(font)
        self.centralwidget = QtWidgets.QWidget(ToolUPSP)
        self.centralwidget.setObjectName("centralwidget")
        self.label_CU = QtWidgets.QLabel(self.centralwidget)
        self.label_CU.setGeometry(QtCore.QRect(30, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_CU.setFont(font)
        self.label_CU.setObjectName("label_CU")
        self.lineUser = QtWidgets.QLineEdit(self.centralwidget)
        self.lineUser.setGeometry(QtCore.QRect(230, 20, 561, 31))
        self.lineUser.setObjectName("lineUser")
        self.label_CI = QtWidgets.QLabel(self.centralwidget)
        self.label_CI.setGeometry(QtCore.QRect(30, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_CI.setFont(font)
        self.label_CI.setObjectName("label_CI")
        self.btUpImage = QtWidgets.QPushButton(self.centralwidget)
        self.btUpImage.setGeometry(QtCore.QRect(230, 70, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btUpImage.setFont(font)
        self.btUpImage.setObjectName("btUpImage")
        self.label_TB = QtWidgets.QLabel(self.centralwidget)
        self.label_TB.setGeometry(QtCore.QRect(30, 150, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_TB.setFont(font)
        self.label_TB.setObjectName("label_TB")
        self.textTB = QtWidgets.QTextEdit(self.centralwidget)
        self.textTB.setGeometry(QtCore.QRect(230, 130, 551, 87))
        self.textTB.setObjectName("textTB")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 260, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 260, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        ToolUPSP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ToolUPSP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 33))
        self.menubar.setObjectName("menubar")
        ToolUPSP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ToolUPSP)
        self.statusbar.setObjectName("statusbar")
        ToolUPSP.setStatusBar(self.statusbar)

        self.retranslateUi(ToolUPSP)
        QtCore.QMetaObject.connectSlotsByName(ToolUPSP)

    def retranslateUi(self, ToolUPSP):
        _translate = QtCore.QCoreApplication.translate
        ToolUPSP.setWindowTitle(_translate("ToolUPSP", "MainWindow"))
        self.label_CU.setText(_translate("ToolUPSP", "Chọn User Chrome"))
        self.label_CI.setText(_translate("ToolUPSP", "Chọn Ảnh"))
        self.btUpImage.setText(_translate("ToolUPSP", "Tải Ảnh"))
        self.label_TB.setText(_translate("ToolUPSP", "Thông báo "))
        self.pushButton.setText(_translate("ToolUPSP", "Start"))
        self.pushButton_2.setText(_translate("ToolUPSP", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ToolUPSP = QtWidgets.QMainWindow()
    ui = Ui_ToolUPSP()
    ui.setupUi(ToolUPSP)
    ToolUPSP.show()
    sys.exit(app.exec_())
