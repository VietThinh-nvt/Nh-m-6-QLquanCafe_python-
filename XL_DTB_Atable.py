import sqlite3


class Database_Atable:
    def __init__(self, db_name="A_DTB_QL_goi.db"):
        self.conn = sqlite3.connect(db_name)
        self.db_name = db_name  # Lưu tên cơ sở dữ liệu


    def LDL_a_tb( self ):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM A_table')
            # for row in cursor.fetchall():
            #     print(row)
            result = cursor.fetchall()
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def Sua_Atb(self, Ten, start_1, start_2, start_3, Trang_thai ):
        try:
            cursor = self.conn.cursor()
            # Câu lệnh SQL để cập nhật thông tin nhân viên
            sql_update_query = '''UPDATE A_table
                                      SET start_1 = ?, start_2 = ?, start_3 = ?, Trang_thai = ?
                                      WHERE Ten = ?'''

            # Thực hiện câu lệnh SQL với dữ liệu đầu vào
            cursor.execute(sql_update_query, (start_1, start_2, start_3, Trang_thai,Ten ))

            self.conn.commit()
            cursor.close()
            print(f"Deleted student with code: {Ten}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()  # Rollback any changes if an error occurs


    def search_student(self, Name):
        try:
            cursor = self.conn.cursor()
            query = "SELECT student_code, name FROM students WHERE name LIKE ?"
            cursor.execute(query, ('%' + Name + '%',))
            #cursor.execute('SELECT * FROM students WHERE student_code,name LIKE ?', ('%' + Name+ '%',))
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def get_all_students(self):
        try:
            cursor = self.conn.cursor()
            query = "SELECT student_code, name FROM students ORDER BY student_code"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def student_exists(self, student_code):
        try:
            cursor = self.conn.cursor()
            query = "SELECT 1 FROM students WHERE student_code = ?"
            cursor.execute(query, (student_code,))
            result = cursor.fetchone()
            cursor.close()
            return result is not None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def add_student(self, student_code, student_name):
        if self.student_exists(student_code):
            print(f"Student with code {student_code} already exists.")
            return False

        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO students (student_code, name) VALUES (?, ?)"
            cursor.execute(query, (student_code, student_name))
            self.conn.commit()
            cursor.close()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()  # Rollback any changes if an error occurs
            return False

    def delete_student(self, student_code):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM students WHERE student_code = ?", (student_code,))
            self.conn.commit()
            cursor.close()
            print(f"Deleted student with code: {student_code}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()  # Rollback any changes if an error occurs



    def __del__(self):
        if self.conn:
            self.conn.close()
