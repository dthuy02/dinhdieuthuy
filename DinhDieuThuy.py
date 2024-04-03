# Đề bài: Đọc 1 file văn bản gồm nhiều dòng 
#         Ghi ra màn hình theo thứ tự ngược lại của các dòng
# VD: Nam quốc sơn hà 
#     Nam đế cư
#     > 
#     Nam đế cư
#     Nam quốc sơn hà

import sys
# Mở file để đọc
file_path = "test.txt"
with open(file_path, "read") as file:
    # Đọc từng dòng trong file và lưu vào danh sách
    lines = file.readlines()

# In danh sách dòng theo thứ tự đảo ngược
for line in reversed(lines):
    print(line.strip())

# Đóng file sau khi đọc xong
file.close()