import sqlite3


class Database_Atable:
    def __init__(self, db_name="A_DTB_QL_goi.db"):
        self.conn = sqlite3.connect(db_name)
        self.db_name = db_name  # Lưu tên cơ sở dữ liệu


    def Goi_mon_DTB( self,Ten_ban, ID_mon, So_luong, HT ):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''INSERT INTO A_table_goi (Ten_ban, ID_mon,So_luong, HT) 
                                      VALUES (?, ?, ?, ?)''',(Ten_ban, ID_mon, So_luong, HT))
            self.conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(f"Database errorlllll: {e}")
            self.conn.rollback()  # Rollback any changes if an error occurs

    def Huy_mon( self,Ten_ban, ID_mon ):
        try:
            cursor = self.conn.cursor()
            # Xóa dữ liệu từ bảng lich_su
            cursor.execute('''
                    DELETE FROM A_table_goi
                    WHERE Ten_ban = ? AND ID_mon = ?
                ''', (Ten_ban, ID_mon))
            self.conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(f"Database errorlllll: {e}")
            self.conn.rollback()

    def Len_mon( self,Ten_ban, ID_mon,HT  ):
        try:
            cursor = self.conn.cursor()
            # Sửa dữ liệu trong bảng lich_su
            cursor.execute('''
                   UPDATE A_table_goi
                   SET HT = ?
                   WHERE Ten_ban = ? AND ID_mon = ?
               ''', (HT,Ten_ban, ID_mon))
            self.conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(f"Database errorlllll: {e}")
            self.conn.rollback()

    def Tim_mon(self, Ten_ban, ID_mon):
        try:
            cursor = self.conn.cursor()
            query = '''
            SELECT Ten_ban, ID_mon,So_luong,HT
            FROM A_table_goi
             WHERE Ten_ban = ? AND ID_mon = ? 
            '''
            cursor.execute(query, (Ten_ban, ID_mon))
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def DL_A_table(self, Name):
        try:
            cursor = self.conn.cursor()
            query = '''
            SELECT A_table_goi.ID_mon,a_menu_db.Name, So_luong, HT, a_menu_db.Gia
            FROM A_table_goi INNER JOIN a_menu_db ON A_table_goi.ID_mon = a_menu_db.ID
            WHERE A_table_goi.Ten_ban = ?
            '''
            cursor.execute(query, ( Name,))
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    def Xoa_table_goi(self, NameTb):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM A_table_goi WHERE Ten_ban = ?", (NameTb,))
            self.conn.commit()
            cursor.close()
            print(f"Deleted A_table_goi with Ten_ban: {NameTb}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()

    def __del__(self):
        if self.conn:
            self.conn.close()
