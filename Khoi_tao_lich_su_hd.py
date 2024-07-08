import sqlite3


conn = sqlite3.connect('A_DTB_QL_goi.db')
cursor = conn.cursor()

# Tạo bảng lich_su
cursor.execute('''
    CREATE TABLE lich_su (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        NameTb TEXT,
        NameK TEXT,
        thoi_gian TIME,
        Ngay DATE,
        Tong_tien FLOAT
    )
''')

# Chèn dữ liệu mẫu
values_to_insert = [
    ('Table 01', 'K1', '10:30', '08-07-2023', 10000),
    ('Table 02', 'K2', '11:00', '02-03-2023', 15000),
    ('Table 03', 'K3', '12:15', '28-09-2023', 20000),
    ('Table 04', 'K4', '13:45', '14-12-2023', 25000),
    ('Table 05', 'K5', '14:30', '23-02-2023', 30000)
]
# Kiểm tra bảng rỗng và chèn dữ liệu mẫu
cursor.execute("SELECT COUNT(*) FROM lich_su")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO lich_su (NameTb, NameK, thoi_gian, Ngay, Tong_tien) VALUES (?, ?, ?, ?, ?)", values_to_insert)

cursor.execute('SELECT * FROM lich_su')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Lưu các thay đổi
conn.commit()
# Đóng kết nối
conn.close()
