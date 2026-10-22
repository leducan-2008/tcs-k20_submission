ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))  
so_phut = int(input("Nhap so phut: "))  
dien_nang_kwh = (cong_suat_w * so_phut) / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")
# Mo ta loi 1:
# - So dong: dong 2 (cong_suat_w = input(...)
# - Thong bao loi (Traceback): unsupported operand type(s) for *: 'str' and 'int' (hoac loi khi nhan chuoi voi so)
# - Nguyen nhan: Ham input() tra ve kieu du lieu chuoi (str), khi dem di nhan hoac chia truc tiep trong bieu thuc toan hoc se gay loi khong tuong thich kieu du lieu.
# - Cach sua: Boc them ham float() hoac int() ben ngoai ham input().
# Mo ta loi 2:
# - So dong: dong 3 (so_phut = input(...))
# - Thong bao loi (Traceback): TypeError: can't multiply sequence by non-int of type 'float'
# - Nguyen nhan: Bien so_phut nhan gia tri tu input() duoi dang chuoi (str) dan den phep tinh toan hoc ben duoi bi loi kieu.
# - Cach sua: Su dung ham int() de chuyen doi du lieu nhap vao thanh so nguyen truoc khi tinh toan