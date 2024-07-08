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
    CREATE TABLE IF NOT EXISTS luong_thang_nv_db (
        id INTEGER ,
        Thang INTEGER,
        Ngay_cong INTEGER
    )
    ''')

    nhan_vien_data = [
        (1, 2, 28),
        (2, 2, 28),
        (3, 2, 28),
        (4, 2, 28),
        (5, 2, 28),
        (1, 3, 28),
        (2, 3, 28),
        (3, 3, 28),
        (4, 3, 28),
        (5, 3, 28),
        (1, 4, 28),
        (2, 4, 28),
        (3, 4, 28),
        (4, 4, 28),
        (5, 4, 28),
        (1, 5, 28),
        (2, 5, 28),
        (3, 5, 28),
        (4, 5, 28),
        (5, 5, 28),

    ]
    # Kiểm tra bảng rỗng và chèn dữ liệu mẫu
    cursor.execute("SELECT COUNT(*) FROM luong_thang_nv_db")
    if cursor.fetchone()[0] == 0:
        # Chèn dữ liệu vào bảng
        cursor.executemany('''
        INSERT INTO luong_thang_nv_db (id, Thang, Ngay_cong)
        VALUES (?, ?, ?)
        ''', nhan_vien_data)
    cursor.execute('SELECT * FROM luong_thang_nv_db')
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    # Commit và đóng kết nối
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created and sample data inserted.")
