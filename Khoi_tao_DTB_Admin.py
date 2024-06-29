import sqlite3
#pyuic6 -x Home.ui -o Home.py
#pyuic6 -x Home_btl.ui -o Home_btl.py
#pyuic6 -x Menu_goi.ui -o Menu_goi.py
#pyuic6 -x A_Table.ui -o gd_A_Table.py
def create_database():
    # Kết nối tới cơ sở dữ liệu (nếu chưa có, tệp sẽ được tạo)
    conn = sqlite3.connect("admin_db.db")
    cursor = conn.cursor()

    # Tạo bảng users với cột Name là khóa chính
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin_db (
        Name TEXT PRIMARY KEY,
        pass TEXT
    )
    ''')

    # Chèn dữ liệu mẫu
    sample_admins = [
        ("admin1", "123"),
        ("admin2", "123"),
        ("admin3", "123"),
        ("admin4", "123"),
        ("admin5", "123"),
    ]
    # Kiểm tra bảng rỗng và chèn dữ liệu mẫu
    cursor.execute("SELECT COUNT(*) FROM admin_db")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO admin_db (Name, pass) VALUES (?, ?)", sample_admins)

    cursor.execute('SELECT * FROM admin_db')
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    # Commit và đóng kết nối
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created and sample data inserted.")
