cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
# Tinh dien nang tieu thu va chi phi
dien_nang_kwh = (cong_suat_w * so_phut) / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
# In gia tri va kieu du lieu
print("Dien nang (kWh):", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phi (VND):", chi_phi, type(chi_phi))
# Thay so_phut thanh 60 roi chay lai so sanh
so_phut_moi = 60
dien_nang_moi = (cong_suat_w * so_phut_moi) / 60 / 1000
chi_phi_moi = dien_nang_moi * don_gia_kwh
print("Khi so phut = 60 -> Dien nang:", dien_nang_moi, "| Chi phi:", chi_phi_moi)
# 15. Du doan ket qua truoc khi chay:
# - Dien nang = (250 * 90) / 60 / 1000 = 22500 / 60000 = 0.375 kWh
# - Chi phi = 0.375 * 3000 = 1125.0 VND