#pyuic6 -x From_Member.ui -o From_Member1.py
#pyuic6 -x Home_btl.ui -o gd_Home1.py
#pyuic6 -x Menu_goi.ui -o gd_Menu_goi.py
#pyuic6 -x A_Table.ui -o gd_A_Table.py
#pyuic6 -x Hoa_don.ui -o gd_Hoa_don.py
#pyuic6 -x Ghi_chu.ui -o gd_Ghi_chu.py
#pyuic6 -x Them_NV.ui -o Them_NV.py

import sys, sqlite3
from functools import partial
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem  # ,QDialog,QMessageBox
from PyQt6.QtCore import QTime

import gd_Dang_nhap, gd_Home1, gd_A_Table, gd_Menu_goi, gd_Hoa_don, gd_Ghi_chu
import TV_DTB, XL_DTB_Atable, XL_DTB_A_menu, XL_DTB_Atb_goi, XL_lich_su_hd


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        self.uic_DN = gd_Dang_nhap.Ui_MainWindow()
        self.uic_Home = gd_Home1.Ui_MainWindow()
        self.uic_Atb = gd_A_Table.Ui_MainWindow()
        self.uic_menu_g = gd_Menu_goi.Ui_MainWindow()
        self.uic_Hoa_don = gd_Hoa_don.Ui_MainWindow()
        self.uic_Ghi_chu = gd_Ghi_chu.Ui_MainWindow()
        self.uic_XL_A_tb = XL_DTB_Atable.Database_Atable("A_DTB_QL_goi.db")
        self.uic_XL_mnu = XL_DTB_A_menu.Database_Atable("A_DTB_QL_goi.db")
        self.uic_XL_tb_goi = XL_DTB_Atb_goi.Database_Atable("A_DTB_QL_goi.db")
        self.uic_XL_ls_hd = XL_lich_su_hd.Database_Atable("A_DTB_QL_goi.db")


        self.uic_TV = TV_DTB.DatabaseSV("admin_db.db")
        self.a = 0
        self.From_DN()



    def From_DN(self):
        self.uic_DN.setupUi(self)
        self.uic_DN.Dang_nhap_bt.clicked.connect(self.xl_Dang_nhap)

    def From_Home(self):
        self.uic_Home.setupUi(self)
        dl = self.uic_XL_ls_hd.LDL_lich_su_hd()
        dl_nv = self.uic_TV.Show_nv()
        self.Loat_home()
        self.Loat_home2(dl)
        self.Loat_home4(dl_nv)
        for i in range(6):
            self.uic_Home.buttons[i].clicked.connect(lambda checked, i=i: self.From_A_Table(i))
        self.uic_Home.bt_tim_kiem.clicked.connect(self.SK_tim_kiem_ls)
        self.uic_Home.bt_Xoa_ls.clicked.connect(self.SK_xoa_ls)
        self.uic_Home.bt_Thong_ke.clicked.connect(self.Sk_Thong_ke)
        self.uic_Home.bt_Tim_kiem_nv.clicked.connect(self.Sk_Tim_nv)
        self.uic_Home.bt_Them_nv.clicked.connect(self.SK_Them_nv)

    def Sk_Thong_ke(self):
        if self.a == 0:
            self.a=1
        else:
            self.a=0
        self.SK_tim_kiem_ls()




    def Loat_home(self):
        dl = self.uic_XL_A_tb.LDL_a_tb()
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

    def Loat_home2(self, dl):
        self.uic_Home.table_lich_su_thanhToant.setRowCount(len(dl))

        for row, (id, name_tb, name_k, thoi_gian, ngay, tong_tien) in enumerate(dl):
            self.uic_Home.table_lich_su_thanhToant.setItem(row, 0, QTableWidgetItem(str(id)))
            self.uic_Home.table_lich_su_thanhToant.setItem(row, 1, QTableWidgetItem(name_tb))
            self.uic_Home.table_lich_su_thanhToant.setItem(row, 2, QTableWidgetItem(name_k))
            self.uic_Home.table_lich_su_thanhToant.setItem(row, 3, QTableWidgetItem(str(thoi_gian)))
            self.uic_Home.table_lich_su_thanhToant.setItem(row, 4, QTableWidgetItem(str(ngay)))
            self.uic_Home.table_lich_su_thanhToant.setItem(row, 5, QTableWidgetItem(str(tong_tien)))

    def Loat_home4(self, dl):
        self.uic_Home.tb_QL_NV.setRowCount(len(dl))

        for row, (id, Ten, Tuoi, Gioi_tinh,Que, luong_ngay, NameTK, pas) in enumerate(dl):
            self.uic_Home.tb_QL_NV.setItem(row, 0, QTableWidgetItem(str(id)))
            self.uic_Home.tb_QL_NV.setItem(row, 1, QTableWidgetItem(str(Ten)))
            self.uic_Home.tb_QL_NV.setItem(row, 2, QTableWidgetItem(str(Tuoi)))
            self.uic_Home.tb_QL_NV.setItem(row, 3, QTableWidgetItem(str(Gioi_tinh)))
            self.uic_Home.tb_QL_NV.setItem(row, 4, QTableWidgetItem(str(Que)))
            self.uic_Home.tb_QL_NV.setItem(row, 5, QTableWidgetItem(str(luong_ngay)))
            self.uic_Home.tb_QL_NV.setItem(row, 6, QTableWidgetItem(str(NameTK)))

    def SK_Them_nv(self):
        d=5
        
    def Sk_Tim_nv(self):

        id = self.uic_Home.txt_ID_nv.text()
        name = self.uic_Home.txt_Ten_nv.text()
        if id != "":
            dl = self.uic_TV.TK_id_nv(id)
        else:
            dl = self.uic_TV.TK_Ten_nv(name)
        self.Loat_home4(dl)
        if id != "":
            d=5
            self.uic_Home.txt_Ten_nv.setText(dl[0][1])
            self.uic_Home.txt_Tuoi_nv.setValue(dl[0][2])
            self.uic_Home.txt_Que_nv.setText(dl[0][4])
            if dl[0][3] == "nam":
                d=5
                self.uic_Home.bt_Gt_nam.setChecked(True)
            else:
                self.uic_Home.bt_Gt_nu.setChecked(True)

    def SK_tim_kiem_ls(self):
        Ten = self.uic_Home.txt_Name.text()
        if Ten != "":
            dl = self.uic_XL_ls_hd.TK_ls_id(Ten)
            if dl == []:
                dl = self.uic_XL_ls_hd.TK_table(Ten)
            if dl == []:
                dl = self.uic_XL_ls_hd.TK_Khach(Ten)
        else:
            Ngay_1 = self.uic_Home.txt_Ngay_1.date().toString('dd-MM-yyyy')#yyyy-MM-dd
            Ngay_2 = self.uic_Home.txt_Ngay_2.date().toString("dd-MM-yyyy")#dd-MM-yyyy
            dl = self.uic_XL_ls_hd.tim_kiem_lich_su_ab(Ngay_1,Ngay_2)
        tien_tk = 0
        float(tien_tk)
        for i in range(len(dl)):
            tien_tk += float(dl[i][5])
        self.Loat_home2(dl)
        if self.a == 0:
            tien_tke = (str(tien_tk)+" VND")
            self.uic_Home.txt_Thong_ke.setText(tien_tke)
            print(tien_tk)
        else:
            self.uic_Home.txt_Thong_ke.setText(str(len(dl)))



    def SK_xoa_ls(self):
        d=5
        id = self.uic_Home.txt_Name.text()
        self.uic_XL_ls_hd.Xoa_ls(id)
        dl = self.uic_XL_ls_hd.LDL_lich_su_hd()
        self.Loat_home2(dl)



    def From_A_Table(self,idex):
        Ntb=("Table 0"+str(idex+1))
        dl = self.uic_XL_tb_goi.DL_A_table(Ntb)
        self.uic_Atb.setupUi(self)
        self.uic_Atb.Text_lb.setText(Ntb)
        self.Loat_A_Table(idex)
        self.update_table1(dl)
        self.uic_Atb.bt_Luu.clicked.connect(partial(self.SK_luu_atb, idex))
        self.uic_Atb.bt_Sua.clicked.connect( self.SK_sua)
        self.uic_Atb.bt_Goi.clicked.connect(partial(self.From_goi_mon, idex))
        self.uic_Atb.bt_Thanh_toan.clicked.connect(partial(self.From_hoa_don, idex))
        self.uic_Atb.bt_Huy_mon.clicked.connect(partial(self.SK_huy_mon, idex))
        self.uic_Atb.bt_Len_mon.clicked.connect(partial(self.SK_Len_mon, idex))
        self.uic_Atb.Chu_thich_1.clicked.connect(partial(self.From_Ghi_chu, idex, 0))
        self.uic_Atb.Chu_thich_2.clicked.connect(partial(self.From_Ghi_chu, idex, 1))
        self.uic_Atb.Chu_thich_3.clicked.connect(partial(self.From_Ghi_chu, idex, 2))


    def From_Ghi_chu(self, idex, i):
        self.uic_Ghi_chu.setupUi(self)
        Ntb = ("Table 0" + str(idex + 1))
        N_ghc = ("Ghi chú "+Ntb)
        dl = self.uic_XL_A_tb.Tim_table(Ntb)
        self.uic_Ghi_chu.txt_Table_ghc.setText(N_ghc)
        self.uic_Ghi_chu.txt_ngay_ghc.setText(str(dl[0][i]))
        self.uic_Ghi_chu.tb_plainTextEdit.setPlainText(dl[0][i+4])

        self.uic_Ghi_chu.bt_Luu.clicked.connect(partial(self.SK_Luu_ghi_c, idex, i))
        self.uic_Ghi_chu.bt_Thoat.clicked.connect(partial(self.From_A_Table, idex))

    def SK_Luu_ghi_c(self, idex, i):
        Ntb = ("Table 0" + str(idex + 1))
        dl = self.uic_XL_A_tb.Tim_table(Ntb)
        ghc = self.uic_Ghi_chu.tb_plainTextEdit.toPlainText()
        if i == 0:
            self.uic_XL_A_tb.Sua_Atb(Ntb,dl[0][0],dl[0][1],dl[0][2],dl[0][3],ghc,dl[0][5],dl[0][6])
        elif i == 1:
            self.uic_XL_A_tb.Sua_Atb(Ntb, dl[0][0], dl[0][1], dl[0][2], dl[0][3], dl[0][4], ghc, dl[0][6])
        elif i == 2:
            print("nnnnnbznz")
            self.uic_XL_A_tb.Sua_Atb(Ntb, dl[0][0], dl[0][1], dl[0][2], dl[0][3], dl[0][4], dl[0][5], ghc)


    def From_hoa_don(self, idex):
        self.uic_Hoa_don.setupUi(self)
        self.Loat_hoadon(idex)
        self.uic_Hoa_don.bt_huy.clicked.connect(partial(self.From_A_Table, idex))
        self.uic_Hoa_don.bt_Thanh_toan.clicked.connect(partial(self.SK_thanh_toan, idex))

    def SK_huy_mon(self, idex):
        Ntb = ("Table 0" + str(idex + 1))
        id = self.uic_Atb.lineEdit.text()
        self.uic_XL_tb_goi.Huy_mon(Ntb,id)
        dl = self.uic_XL_tb_goi.DL_A_table(Ntb)
        self.update_table1(dl)

    def SK_Len_mon(self,idex):
        d=5
        Ntb = ("Table 0" + str(idex + 1))
        id = self.uic_Atb.lineEdit.text()
        mon = self.uic_XL_tb_goi.Tim_mon(Ntb,id)
        print(mon)
        if mon != []:
            hoan_thanh = mon[0][3]
            if mon[0][3] < mon[0][2]:
                d=5
                hoan_thanh = (mon[0][3] + 1)
            self.uic_XL_tb_goi.Len_mon(Ntb,id,hoan_thanh)
        dl = self.uic_XL_tb_goi.DL_A_table(Ntb)
        self.update_table1(dl)

    def Loat_hoadon(self,idex):
        Ntb = ("Table 0" + str(idex + 1))
        N_hd = ("Hóa đơn "+ Ntb)
        self.uic_Hoa_don.txt_hoa_don1.setText(N_hd)
        dl = self.uic_XL_tb_goi.DL_A_table(Ntb)
        Thanh_tien = []
        tong_tien = 0
        for i in range(len(dl)) :
            tien =float(dl[i][2]) * float(dl[i][4])
            Thanh_tien.append(tien)
            tong_tien += tien
        txt_tong_tien = (" Tổng tiền "+str(tong_tien) +" VND")
        # chen dl vào table
        self.uic_Hoa_don.Table_hoa_don.setRowCount(len(dl))
        for row, (ID_mon,Name, So_luong, HT,Gia) in enumerate(dl):
            self.uic_Hoa_don.Table_hoa_don.setItem(row, 0, QTableWidgetItem(Name))
            self.uic_Hoa_don.Table_hoa_don.setItem(row, 1, QTableWidgetItem(str(So_luong)))
        for row, (tien) in enumerate(Thanh_tien):
            self.uic_Hoa_don.Table_hoa_don.setItem(row, 2, QTableWidgetItem(str(tien)))
        self.uic_Hoa_don.txt_tong_tien.setText(txt_tong_tien)

    def SK_thanh_toan(self, idex):
        d= 5
        Ntb = ("Table 0" + str(idex + 1))
        NameK= ""
        ngay = datetime.now().strftime('%d-%m-%Y')
        dl_A_Tble = self.uic_XL_A_tb.Tim_table(Ntb)
        thoi_gian =dl_A_Tble[0][0]
        dl = self.uic_XL_tb_goi.DL_A_table(Ntb)
        tong_tien = 0
        for i in range(len(dl)):
            tien = float(dl[i][2]) * float(dl[i][4])
            tong_tien += tien
        self.uic_XL_ls_hd.Them_ls(Ntb, NameK, thoi_gian, ngay, tong_tien)
        self.uic_XL_tb_goi.Xoa_table_goi(Ntb)
        self.uic_XL_A_tb.Sua_Atb(Ntb, dl_A_Tble[0][1], dl_A_Tble[0][2], "00:00:00", dl_A_Tble[0][3],  dl_A_Tble[0][5], dl_A_Tble[0][6], "")

        self.From_A_Table(idex)


    def From_goi_mon(self, idex):
        self.uic_menu_g.setupUi(self)
        self.Loat_from_goi()
        self.uic_menu_g.bt_Luu.clicked.connect(partial(self.SK_luu_goi_mon, idex,2))
        self.uic_menu_g.bt_Luu_2.clicked.connect(partial(self.SK_luu_goi_mon, idex,1))

    def SK_luu_goi_mon(self, idex,luu):
        d=5
        if luu == 1:
            n = 0
        else:
            n = 8
        Ntb=("Table 0"+str(idex+1))
        dl = self.uic_XL_mnu.LDL_a_tb()
        for i in range(n, n+8):

            id = dl[i][0]
            sl = int(self.uic_menu_g.bt_goi_n[i].text())

            if sl > 0 :
                self.uic_XL_tb_goi.Goi_mon_DTB(Ntb,id,sl,0)

        self.From_A_Table(idex)



    def Loat_from_goi(self):
        d=5
        dl = self.uic_XL_mnu.LDL_a_tb()
        for i in range(16):
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

    def update_table1(self, data):
        self.uic_Atb.tableWidget.setRowCount(len(data))
        for row, (ID, Name, so_luong, Hoan_thanh, gia)  in enumerate(data):
            self.uic_Atb.tableWidget.setItem(row, 0, QTableWidgetItem(ID))
            self.uic_Atb.tableWidget.setItem(row, 1, QTableWidgetItem(Name))
            self.uic_Atb.tableWidget.setItem(row, 2, QTableWidgetItem(str(so_luong)))
            self.uic_Atb.tableWidget.setItem(row, 3, QTableWidgetItem(str(Hoan_thanh)))


    def Loat_A_Table(self, i):
        dl = self.uic_XL_A_tb.LDL_a_tb()
        # Chuyển đổi chuỗi a thành QTime
        time_star1 = dl[i][1].split(':')
        if len(time_star1) == 3:
            hours, minutes, seconds = map(int, time_star1)
            time1 = QTime(hours, minutes, seconds)
            self.uic_Atb.time_start_1.setTime(time1)
        else:
            print("Invalid time format")

        time_star2 = dl[i][2].split(':')
        if len(time_star2) == 3:
            hours, minutes, seconds = map(int, time_star2)
            time2 = QTime(hours, minutes, seconds)
            self.uic_Atb.time_start_2.setTime(time2)
        else:
            print("Invalid time format")

        time_star3 = dl[i][3].split(':')
        if len(time_star3) == 3:
            hours, minutes, seconds = map(int, time_star3)
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
        if self.uic_Atb.Check_trong.isChecked():
            check = 0
        elif self.uic_Atb.Check_dat.isChecked():
            check = 1
        elif self.uic_Atb.Check_coKH.isChecked():
            check = 2
        self.uic_XL_A_tb.Sua_Atb(Ten, star1_str, star2_str, star3_str, check, "", "", "")

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
