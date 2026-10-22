tong_phut = 135
cong_suat_w = 250
# Dung // va % de tinh so gio tron ven va so phut con lai
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print(f"135 phut = {so_gio} gio {so_phut_du} phut")
# Tao bien boolean
su_dung_lau = tong_phut > 60
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Su dung lau hon 60 phut:", su_dung_lau)
print("Du lieu hop le:", du_lieu_hop_le)
# Du doan va kiem chung bieu thuc
# 100 + 20 * 3 = 100 + 60 = 160 
print(100 + 20 * 3)
# (100 + 20) * 3 = 120 * 3 = 360 
print((100 + 20) * 3)