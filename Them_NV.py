# Form implementation generated from reading ui file 'Them_NV.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(326, 356)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 0, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_Name_TK_tnv = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_Name_TK_tnv.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.txt_Name_TK_tnv.setObjectName("txt_Name_TK_tnv")
        self.txt_pass_1_tnv = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_pass_1_tnv.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.txt_pass_1_tnv.setObjectName("txt_pass_1_tnv")
        self.txt_pass_2_tnv = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_pass_2_tnv.setGeometry(QtCore.QRect(110, 110, 113, 20))
        self.txt_pass_2_tnv.setObjectName("txt_pass_2_tnv")
        self.txt_Ten_tnv = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_Ten_tnv.setGeometry(QtCore.QRect(110, 150, 113, 20))
        self.txt_Ten_tnv.setObjectName("txt_Ten_tnv")
        self.txt_Tuoi_tnv = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.txt_Tuoi_tnv.setGeometry(QtCore.QRect(110, 180, 42, 22))
        self.txt_Tuoi_tnv.setObjectName("txt_Tuoi_tnv")
        self.cb_Gioi_tinh_tnv = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cb_Gioi_tinh_tnv.setGeometry(QtCore.QRect(170, 180, 53, 22))
        self.cb_Gioi_tinh_tnv.setObjectName("cb_Gioi_tinh_tnv")
        self.cb_Gioi_tinh_tnv.addItem("")
        self.cb_Gioi_tinh_tnv.addItem("")
        self.txt_Que_tnv = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_Que_tnv.setGeometry(QtCore.QRect(110, 220, 113, 20))
        self.txt_Que_tnv.setObjectName("txt_Que_tnv")
        self.bt_Huy_tnv = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_Huy_tnv.setGeometry(QtCore.QRect(100, 260, 56, 17))
        self.bt_Huy_tnv.setObjectName("bt_Huy_tnv")
        self.bt_Them_tnv = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_Them_tnv.setGeometry(QtCore.QRect(170, 260, 56, 17))
        self.bt_Them_tnv.setObjectName("bt_Them_tnv")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 41, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 61, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 180, 61, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 220, 61, 20))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 326, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Thêm Nhân viên"))
        self.cb_Gioi_tinh_tnv.setItemText(0, _translate("MainWindow", "Nam"))
        self.cb_Gioi_tinh_tnv.setItemText(1, _translate("MainWindow", "Nữ"))
        self.bt_Huy_tnv.setText(_translate("MainWindow", "Hủy"))
        self.bt_Them_tnv.setText(_translate("MainWindow", "Thêm"))
        self.label_2.setText(_translate("MainWindow", "Name TK"))
        self.label_3.setText(_translate("MainWindow", "pass"))
        self.label_4.setText(_translate("MainWindow", "Nhạp lại pass"))
        self.label_5.setText(_translate("MainWindow", "Tên"))
        self.label_6.setText(_translate("MainWindow", "Tuổi"))
        self.label_7.setText(_translate("MainWindow", "Quê"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
