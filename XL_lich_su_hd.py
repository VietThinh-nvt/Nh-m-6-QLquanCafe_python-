import sqlite3


class Database_Atable:
    def __init__(self, db_name="A_DTB_QL_goi.db"):
        self.conn = sqlite3.connect(db_name)
        self.db_name = db_name  # Lưu tên cơ sở dữ liệu


    def Them_ls( self,name_tb, name_k, thoi_gian, ngay, tong_tien ):
        try:
            cursor = self.conn.cursor()
            # Thêm dữ liệu vào bảng lich_su
            cursor.execute('''
                  INSERT INTO lich_su (NameTb, NameK, thoi_gian, Ngay, Tong_tien)
                  VALUES (?, ?, ?, ?, ?)
              ''', (name_tb, name_k, thoi_gian, ngay, tong_tien))

            self.conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(f"Database errorlllll: {e}")
            self.conn.rollback()  # Rollback any changes if an error occurs
    def LDL_lich_su_hd( self ):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM lich_su')
            result = cursor.fetchall()
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def tim_kiem_lich_su_ab(self, a, b):
        try:
            cursor = self.conn.cursor()
            query = '''
                    SELECT * FROM lich_su
                    WHERE Ngay BETWEEN ? AND ?
                    '''
            cursor.execute(query, (a, b))
            result = cursor.fetchall()
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def TK_table(self, Name):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM lich_su WHERE NameTb LIKE ?"
            cursor.execute(query, ('%' + Name + '%',))
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def TK_Khach(self, Name):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM lich_su WHERE NameK LIKE ?"
            cursor.execute(query, ('%' + Name + '%',))
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    def TK_ls_id(self, ID):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM lich_su WHERE id = ?"
            cursor.execute(query, (ID,))
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    def Xoa_ls(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM lich_su WHERE id = ?", (id,))
            self.conn.commit()
            cursor.close()
            print(f"Deleted lich_su with id: {id}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()

    def __del__(self):
        if self.conn:
            self.conn.close()
