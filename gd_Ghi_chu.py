# Form implementation generated from reading ui file 'Ghi_chu.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 336)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tb_plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.tb_plainTextEdit.setGeometry(QtCore.QRect(0, 50, 301, 221))
        self.tb_plainTextEdit.setObjectName("tb_plainTextEdit")
        self.bt_Thoat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_Thoat.setGeometry(QtCore.QRect(240, 280, 56, 17))
        self.bt_Thoat.setObjectName("bt_Thoat")
        self.bt_Luu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_Luu.setGeometry(QtCore.QRect(160, 280, 56, 17))
        self.bt_Luu.setObjectName("bt_Luu")
        self.txt_Table_ghc = QtWidgets.QLabel(parent=self.centralwidget)
        self.txt_Table_ghc.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(14)
        self.txt_Table_ghc.setFont(font)
        self.txt_Table_ghc.setObjectName("txt_Table_ghc")
        self.txt_ngay_ghc = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_ngay_ghc.setEnabled(False)
        self.txt_ngay_ghc.setGeometry(QtCore.QRect(190, 30, 113, 20))
        self.txt_ngay_ghc.setObjectName("txt_ngay_ghc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 18))
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
        self.bt_Thoat.setText(_translate("MainWindow", "Thoát"))
        self.bt_Luu.setText(_translate("MainWindow", "Lưu"))
        self.txt_Table_ghc.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
