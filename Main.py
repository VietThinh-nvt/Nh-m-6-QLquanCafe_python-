#pyuic6 -x From_Member.ui -o From_Member1.py
#pyuic6 -x Home_btl.ui -o gd_Home1.py
#pyuic6 -x Menu_goi.ui -o gd_Menu_goi.py
#pyuic6 -x A_Table.ui -o gd_A_Table.py
import sys, sqlite3
from functools import partial
# pip install pyqt5
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem  # ,QDialog,QMessageBox
from PyQt6.QtCore import QTime

import gd_Dang_nhap, gd_Home1, gd_A_Table, gd_Menu_goi
#import Admin, User, Member
import TV_DTB, XL_DTB_Atable, XL_DTB_A_menu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        self.uic_DN = gd_Dang_nhap.Ui_MainWindow()
        self.uic_Home = gd_Home1.Ui_MainWindow()
        self.uic_Atb = gd_A_Table.Ui_MainWindow()
        self.uic_menu_g = gd_Menu_goi.Ui_MainWindow()
        self.uic_XL_Atb = XL_DTB_Atable.Database_Atable("A_DTB_QL_goi.db")
        self.uic_XL_mnu = XL_DTB_A_menu.Database_Atable("A_DTB_QL_goi.db")


        # self.ui_XL = XL_DTB.DatabaseSV()
        # self.ui_Us = User.User()
        self.uic_TV = TV_DTB.DatabaseSV("admin_db.db")
        self.From_DN()

        # self.load_student_data()


    def From_DN(self):
        self.uic_DN.setupUi(self)
        self.uic_DN.Dang_nhap_bt.clicked.connect(self.xl_Dang_nhap)
        #self.ui_XL.Show_ns2()
    def From_Home(self):
        self.uic_Home.setupUi(self)
        self.Loat_home()
        for i in range(6):
            self.uic_Home.buttons[i].clicked.connect(lambda checked, i=i: self.From_A_Table(i))
        #self.uic_Home.

    def Loat_home(self):
        dl = self.uic_XL_Atb.LDL_a_tb()
        #print(dl)
        for i in range(6):
            # Chuyển đổi chuỗi a thành QTime
            time_parts = dl[i][1].split(':')
            if len(time_parts) == 3:
                hours, minutes, seconds = map(int, time_parts)
                time = QTime(hours, minutes, seconds)
                self.uic_Home.Time_n[i].setTime(time)
            else:
                print("Invalid time format")
            if dl[i][4] == 0:
                self.uic_Home.Check_trong_n[i].setChecked(True)
            elif dl[i][4] == 1:
                self.uic_Home.Check_dat_n[i].setChecked(True)
            elif dl[i][4] == 2:
                self.uic_Home.Check_coKh_n[i].setChecked(True)


    def From_A_Table(self, idex):
        d=str(idex+1)
        #self.uic_Home.buttons[]
        self.uic_Atb.setupUi(self)
        self.uic_Atb.Text_lb.setText(("Table 0"+d))
        self.Loat_A_Table(idex)
        self.uic_Atb.bt_Luu.clicked.connect(partial(self.SK_luu_atb, idex))
        self.uic_Atb.bt_Sua.clicked.connect( self.SK_sua)
        self.uic_Atb.bt_Goi.clicked.connect(partial(self.From_goi_mon, idex))

    def From_goi_mon(self, idex):
        d=5
        self.uic_menu_g.setupUi(self)
        self.Loat_from_goi()
        self.uic_menu_g.bt_Luu.clicked.connect(partial(self.From_A_Table, idex))
        self.uic_menu_g.bt_Luu_2.clicked.connect(partial(self.From_A_Table, idex))

    def Loat_from_goi(self):
        d=5
        dl = self.uic_XL_mnu.LDL_a_tb()
        print(dl)
        for i in range(16):
            d=5
            self.uic_menu_g.label_n[i].setText(dl[i][1])




    def xl_Dang_nhap(self):
        try:
            us_name = self.uic_DN.Name_text.text()
            us_pass = self.uic_DN.pass_text.text()

            if us_name == "" or us_pass == "":
                QMessageBox.warning(None, "Cảnh báo", "Vui lòng nhập tên đăng nhập và mật khẩu!")
                return
            login = self.uic_TV.KT_DN(us_name, us_pass)
            print(login)
            if login:
                QMessageBox.information(None, 'Thông báo', 'Đăng nhập thành công!')
                self.From_Home()
                #self.load_student_data()

            else:
                QMessageBox.critical(None, 'Lỗi', 'Đăng nhập thất bại.')

        except sqlite3.Error as e:
            QMessageBox.critical(None, 'Lỗi', f'Lỗi đăng nhập: {str(e)}')






    def Loat_A_Table(self, i):
        dl = self.uic_XL_Atb.LDL_a_tb()
        print("loat dl")
        print(dl)
        # Chuyển đổi chuỗi a thành QTime
        time_star1 = dl[i][1].split(':')
        if len(time_star1) == 3:
            hours, minutes, seconds = map(int, time_star1)
            print(hours+minutes+seconds)
            time1 = QTime(hours, minutes, seconds)
            self.uic_Atb.time_start_1.setTime(time1)
        else:
            print("Invalid time format")

        time_star2 = dl[i][2].split(':')
        if len(time_star2) == 3:
            hours, minutes, seconds = map(int, time_star2)
            time2 = QTime(hours, minutes, seconds)
            print(hours + minutes + seconds)
            self.uic_Atb.time_start_2.setTime(time2)
        else:
            print("Invalid time format")

        time_star3 = dl[i][3].split(':')
        if len(time_star3) == 3:
            hours, minutes, seconds = map(int, time_star3)
            print(hours + minutes + seconds)
            time3 = QTime(hours, minutes, seconds)
            self.uic_Atb.time_start_3.setTime(time3)
        else:
            print("Invalid time format")

        if dl[i][4] == 0:
            self.uic_Atb.Check_trong.setChecked(True)
        elif dl[i][4] == 1:
            self.uic_Atb.Check_dat.setChecked(True)
        elif dl[i][4] == 2:
            self.uic_Atb.Check_coKH.setChecked(True)


    def SK_luu_atb(self, i):
        check = 0
        Ten = "Table 0"+str(i+1)
        star1 = self.uic_Atb.time_start_1.time()
        star1_str = star1.toString('HH:mm:ss')
        star2 = self.uic_Atb.time_start_2.time()
        star2_str = star2.toString('HH:mm:ss')
        star3 = self.uic_Atb.time_start_3.time()
        star3_str = star3.toString('HH:mm:ss')
        #print(star1_str)
        #print(star2_str)
        #print(star3_str)

        if self.uic_Atb.Check_trong.isChecked():
            check = 0
        elif self.uic_Atb.Check_dat.isChecked():
            check = 1
        elif self.uic_Atb.Check_coKH.isChecked():
            check = 2
        self.uic_XL_Atb.Sua_Atb(Ten, star1_str, star2_str, star3_str, check )

        self.From_Home()


    def SK_sua(self):
        d=5
        if self.uic_Atb.time_start_1.isEnabled():
            self.uic_Atb.time_start_1.setEnabled(False)
            self.uic_Atb.time_start_2.setEnabled(False)
            self.uic_Atb.time_start_3.setEnabled(False)
            self.uic_Atb.Check_trong.setEnabled(False)
            self.uic_Atb.Check_dat.setEnabled(False)
            self.uic_Atb.Check_coKH.setEnabled(False)
        else:
            self.uic_Atb.time_start_1.setEnabled(True)
            self.uic_Atb.time_start_2.setEnabled(True)
            self.uic_Atb.time_start_3.setEnabled(True)
            self.uic_Atb.Check_trong.setEnabled(True)
            self.uic_Atb.Check_dat.setEnabled(True)
            self.uic_Atb.Check_coKH.setEnabled(True)


    '''
    def Them_DL(self):
        d = 5
        # tmb = Member.Member()
        Name = self.ui_FM.TimKiem_text.text()
        # Tmb = Member.Member.register("ffg","ggh" )
        # print(Tmb )

    def LDL(self):
        # self.ui_H.setupUi(self)
        Name = self.ui_FM.TimKiem_text.text()
        print("?", (Name))
        try:
            result = self.ui_XL.search_student(Name)
            if result:
                self.update_table1(result)
                # self.accept()
            else:
                # QtWidgets
                QMessageBox.warning(self, "Warning", "Khong tim thay sinh vien")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error during search: {e}")

    def load_student_data(self):
        result = self.ui_XL.get_all_students()
        self.update_table1(result)
        self.ui_FM.table_Member.resizeColumnsToContents()

    def update_table1(self, data):
        self.ui_FM.table_Member.setRowCount(len(data))
        for row, (id_, name) in enumerate(data):
            self.ui_FM.table_Member.setItem(row, 0, QTableWidgetItem(str(id_)))
            self.ui_FM.table_Member.setItem(row, 1, QTableWidgetItem(name))


    '''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
