# Nhan bon gia tri qua input() va in type() ngay sau khi nhap
ma_may_in = input("Nhap ma may: ")
print(type(ma_may_in))
cong_suat_in = input("Nhap cong suat W: ")
print(type(cong_suat_in))
so_phut_in = input("Nhap so phut: ")
print(type(so_phut_in))
don_gia_in = input("Nhap don gia: ")
print(type(don_gia_in))
# Chuyen doi kieu du lieu
cong_suat_w = float(cong_suat_in)
so_phut = int(so_phut_in)
don_gia_kwh = float(don_gia_in)
# Tinh lai dien nang va chi phi sau khi chuyen kieu
dien_nang_kwh = (cong_suat_w * so_phut) / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Dien nang tieu thu:", dien_nang_kwh)
print("Chi phi dien:", chi_phi)