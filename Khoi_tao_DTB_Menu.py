import sqlite3
#pyuic6 -x Home.ui -o Home.py
#pyuic6 -x Home_btl.ui -o Home_btl.py
#pyuic6 -x Menu_goi.ui -o Menu_goi.py
def create_database():
    # Kết nối tới cơ sở dữ liệu (nếu chưa có, tệp sẽ được tạo)
    conn = sqlite3.connect("A_DTB_QL_goi.db")
    cursor = conn.cursor()

    # Tạo bảng users với cột Name là khóa chính
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS a_menu_db (
        ID TEXT PRIMARY KEY,
        Name TEXT NOT NULL,
        Gia INTEGER NOT NULL 
    )
    ''')

    # Chèn dữ liệu mẫu
    sample_menu = [
        ("du1", "bạc xỉu", 25000),
        ("du2", "cafe sua", 25000),
        ("du3", "nuoc cam", 25000),
        ("du4", "tranh leo", 25000),
        ("du5", "hông đào", 25000),
        ("du6", "cafe đen", 25000),
        ("du7", "việt quất", 25000),
        ("du8", "sin tố bơ", 25000),
        ("ma1", "hướng dương NB", 25000),
        ("ma2", "hướng dương mặn", 25000),
        ("ma3", "hướng dương  ngọt", 25000),
        ("ma4", "bim bim", 25000),
        ("ma5", "quẩy", 25000),
        ("ma6", "hạt bí", 25000),
        ("ma7", "hạt điều", 25000),
        ("ma8", "nho khô", 25000)

    ]
    # Kiểm tra bảng rỗng và chèn dữ liệu mẫu
    cursor.execute("SELECT COUNT(*) FROM a_menu_db")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO a_menu_db (ID, Name, Gia) VALUES (?, ?, ?)", sample_menu)

    cursor.execute('SELECT * FROM a_menu_db')
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    # Commit và đóng kết nối
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created and sample data inserted.")
