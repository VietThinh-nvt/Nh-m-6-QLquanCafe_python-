# Form implementation generated from reading ui file 'Hoa_don.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 404)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Table_hoa_don = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.Table_hoa_don.setGeometry(QtCore.QRect(90, 40, 281, 261))
        self.Table_hoa_don.setObjectName("Table_hoa_don")
        self.Table_hoa_don.setColumnCount(3)
        self.Table_hoa_don.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Table_hoa_don.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_hoa_don.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_hoa_don.setHorizontalHeaderItem(2, item)
        self.txt_hoa_don1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.txt_hoa_don1.setGeometry(QtCore.QRect(90, 0, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(20)
        self.txt_hoa_don1.setFont(font)
        self.txt_hoa_don1.setObjectName("txt_hoa_don1")
        self.bt_huy = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_huy.setGeometry(QtCore.QRect(90, 340, 91, 21))
        self.bt_huy.setObjectName("bt_huy")
        self.bt_Thanh_toan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_Thanh_toan.setGeometry(QtCore.QRect(280, 340, 91, 21))
        self.bt_Thanh_toan.setObjectName("bt_Thanh_toan")
        self.txt_tong_tien = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_tong_tien.setGeometry(QtCore.QRect(90, 310, 281, 20))
        self.txt_tong_tien.setObjectName("txt_tong_tien")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 18))
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
        item = self.Table_hoa_don.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tên món"))
        item = self.Table_hoa_don.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Số lượng"))
        item = self.Table_hoa_don.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Thành tiền"))
        self.txt_hoa_don1.setText(_translate("MainWindow", "hoa don"))
        self.bt_huy.setText(_translate("MainWindow", "hủy"))
        self.bt_Thanh_toan.setText(_translate("MainWindow", "Xác nhận"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())