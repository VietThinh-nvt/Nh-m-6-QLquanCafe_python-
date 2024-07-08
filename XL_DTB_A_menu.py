import sqlite3


class Database_Atable:
    def __init__(self, db_name="A_DTB_QL_goi.db"):
        self.conn = sqlite3.connect(db_name)
        self.db_name = db_name  # Lưu tên cơ sở dữ liệu


    def LDL_a_tb( self ):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM a_menu_db')
            result = cursor.fetchall()
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []


    def __del__(self):
        if self.conn:
            self.conn.close()
