from datetime import datetime, timedelta
# Phan 1: Thoi diem hien tai va dinh dang
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
# Phan 2: Sau do bo sung (Tinh thoi luong giua hai thoi diem)
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
# 25. Giai thich su khac nhau giua datetime, str va timedelta trong vi du:
# - datetime: La doi tuong dai diện cho ngay va gio (date and time), cho phep thuc hien cac phep toan thoi gian nhu tru nhau de tinh khoang cach.
# - str (String): La chuoi van ban thuan tuy (nhu thoi_diem_text), duoc dung de hien thi hoac luu tru duoi dang ky tu, khong the dung truc tiep de thuc hien cac phep toan toan hoc/thoi gian.
# - timedelta: La doi tuong bieu dien khoang thoi gian hoac do lech thoi gian (hieu so giua hai doi tuong datetime, vi du nhu thoi_luong o tren).