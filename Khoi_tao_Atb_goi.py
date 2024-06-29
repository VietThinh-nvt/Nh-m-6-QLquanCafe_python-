import sqlite3

# pyuic6 -x gd_sua.ui -o gd_sua.py
# Kết nối đến cơ sở dữ liệu SQLite (hoặc tạo một cơ sở dữ liệu mới nếu chưa tồn tại)
conn = sqlite3.connect('A_DTB_QL_goi.db')

# Tạo đối tượng cursor để thao tác với cơ sở dữ liệu
cursor = conn.cursor()

# Tạo bảng "A_table" với các cột và kiểu dữ liệu tương ứng
cursor.execute('''CREATE TABLE IF NOT EXISTS A_table_goi (
                    Ten_ban TEXT ,
                    ID_mon TEXT ,
                    So_luong INTEGER ,
                    HT INTEGER

                )''')

# Chèn dữ liệu vào bảng
data_to_insert = [
    ('Table 01', 'du1', 1, 0),
    ('Table 01', 'du2', 1, 0),
    ('Table 01', 'du3', 1, 0),
    ('Table 01', 'du4', 1, 0),


]

# Sử dụng câu lệnh SQL INSERT để chèn dữ liệu vào bảng

# Kiểm tra bảng rỗng và chèn dữ liệu mẫu
cursor.execute("SELECT COUNT(*) FROM A_table_goi")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''INSERT INTO A_table_goi (Ten_ban, ID_mon, So_luong, HT) 
                          VALUES (?, ?, ?, ?)''', data_to_insert)

cursor.execute('SELECT * FROM A_table_goi')
rows = cursor.fetchall()

for row in rows:
    print(row)
# Commit và đóng kết nối

# Lưu thay đổi và đóng kết nối đến cơ sở dữ liệu
conn.commit()
conn.close()

print("Bảng 'A_table' đã được tạo thành công.")
