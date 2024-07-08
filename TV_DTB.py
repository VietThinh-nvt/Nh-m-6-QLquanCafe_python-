import sqlite3


class DatabaseSV:
    def __init__(self, db_name="admin_db.db"):
        self.conn = sqlite3.connect(db_name)
        self.db_name = db_name  # Lưu tên cơ sở dữ liệu




    def KT_DN(self, Name, pas):
        try:
            cursor = self.conn.cursor()

            query = "SELECT Name, pass FROM admin_db WHERE Name = ? AND pass = ?"
            output = cursor.execute(query, (Name, pas)).fetchone()
            #result = cursor.fetchall()
            result = output
            print(result)
            cursor.close()
            if output is not None:
                self.id = output[0]
                self.logged_in = True
                print(F"Logged in")
                print(result)
            else:
                self.logged_in = False
                print(F"Invalid username or password")
            print("tesst1")
            return self.logged_in
            #return result

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def Show_nv(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM nhan_vien_db')
            result = cursor.fetchall()
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def TK_id_nv(self, ID):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM nhan_vien_db WHERE id = ?"
            cursor.execute(query, (ID,))
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    def TK_Ten_nv(self, Name):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM nhan_vien_db WHERE Ten LIKE ?"
            cursor.execute(query, ('%' + Name + '%',))
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

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

    def Show_ns( self ):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM admin_db')
            for row in cursor.fetchall():
                print(row)
            #conn.close()

            #result = cursor.fetchall()
            cursor.close()
            #return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def __del__(self):
        if self.conn:
            self.conn.close()
