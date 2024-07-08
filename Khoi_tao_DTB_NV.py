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
    CREATE TABLE IF NOT EXISTS nhan_vien_db (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Ten TEXT ,
        Tuoi INTEGER,
        Gioi_tinh TEXT ,
        Que TEXT,
        luong_ngay FLOAT,
        NameTK TEXT ,
        pass TEXT
    )
    ''')

    nhan_vien_data = [
        ('Nguyen thi kim Anh', 30, 'Nam','Ha Nội', 200000, 'anhntk', '123'),
        ('Le Thi Bảo', 25, 'Nu','hạ long', 250000, 'baolt', '123'),
        ('Nguyễn Viết Thịnh ', 24, 'Nam','Bắc giang', 510000, 'ThinhNV', '123'),
        ('Pham Thi Déo', 32, 'Nu','Bắc giang', 180000, 'deopt', '123'),
        ('Hoang Van E', 29, 'Nam','Bắc giang', 210000, 'hoangvane', '123')
    ]
    # Kiểm tra bảng rỗng và chèn dữ liệu mẫu
    cursor.execute("SELECT COUNT(*) FROM nhan_vien_db")
    if cursor.fetchone()[0] == 0:
        # Chèn dữ liệu vào bảng
        cursor.executemany('''
        INSERT INTO nhan_vien_db (Ten, Tuoi, Gioi_tinh,Que, luong_ngay, NameTK, pass)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', nhan_vien_data)
    cursor.execute('SELECT * FROM nhan_vien_db')
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    # Commit và đóng kết nối
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created and sample data inserted.")
