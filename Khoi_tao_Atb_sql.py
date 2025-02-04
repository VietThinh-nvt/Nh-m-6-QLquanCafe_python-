import sqlite3
#pyuic6 -x gd_sua.ui -o gd_sua.py
# Kết nối đến cơ sở dữ liệu SQLite (hoặc tạo một cơ sở dữ liệu mới nếu chưa tồn tại)
conn = sqlite3.connect('A_DTB_QL_goi.db')

# Tạo đối tượng cursor để thao tác với cơ sở dữ liệu
cursor = conn.cursor()

# Tạo bảng "A_table" với các cột và kiểu dữ liệu tương ứng
cursor.execute('''CREATE TABLE IF NOT EXISTS A_table (
                    Ten TEXT PRIMARY KEY,
                    start_1 TIME,
                    Start_2 TIME,
                    Start_3 TIME,
                    Trang_thai INTEGER,
                    Ghi_chu_1 TEXT,
                    Ghi_chu_2 TEXT,
                    Ghi_chu_3 TEXT
                )''')

# Chèn dữ liệu vào bảng
data_to_insert = [
    ('Table 01', '1:00:00', '5:00:00', '6:00:00', 0,'aaa','bbb','ccc'),
    ('Table 02', '3:00:00', '7:00:00', '12:00:00', 2,'ddd','eee','fff'),
    ('Table 03', '9:00:00', '3:00:00', '12:00:00', 2,'ggg','jjj','kkk'),
    ('Table 04', '2:00:00', '12:00:00', '12:00:00', 2,'','',''),
    ('Table 05', '2:00:00', '12:00:00', '12:00:00', 1,'','',''),
    ('Table 06', '8:00:00', '12:00:00', '12:00:00', 0,'','','')

]

# Kiểm tra bảng rỗng và chèn dữ liệu mẫu
cursor.execute("SELECT COUNT(*) FROM A_table")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''INSERT INTO A_table (Ten, start_1, start_2, start_3, Trang_thai,Ghi_chu_1,Ghi_chu_2, Ghi_chu_3)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', data_to_insert)

cursor.execute('SELECT * FROM A_table')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()

print("Bảng 'A_table' đã được tạo thành công.")
