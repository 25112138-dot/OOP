class NhanVien:
    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong

    def inThongTin(self):
        print(f"Tên NV: {self.ten}, Lương: {self.luong}")


class CongTacVien(NhanVien):
    def __init__(self, ten, luong, thoi_han_hd, phu_cap):
        super().__init__(ten, luong)
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap = phu_cap

    def inThongTin(self):
        super().inThongTin()
        print(f"Hợp đồng: {self.thoi_han_hd} tháng, Phụ cấp: {self.phu_cap}")


class NhanVienChinhThuc(NhanVien):
    def __init__(self, ten, luong, vi_tri):
        super().__init__(ten, luong)
        self.vi_tri = vi_tri

    def inThongTin(self):
        super().inThongTin()
        print(f"Vị trí: {self.vi_tri}")


class TruongPhong(NhanVien):
    def __init__(self, ten, luong, ngay_bat_dau, phu_cap_ql):
        super().__init__(ten, luong)
        self.ngay_bat_dau = ngay_bat_dau
        self.phu_cap_ql = phu_cap_ql

    def inThongTin(self):
        super().inThongTin()
        print(f"Ngày bắt đầu quản lý: {self.ngay_bat_dau}, Phụ cấp quản lý: {self.phu_cap_ql}")


# Ví dụ sử dụng
ctv = CongTacVien("Nguyen Van B", 4000, 12, 500)
nvct = NhanVienChinhThuc("Tran Thi C", 8000, "Kế toán")
tp = TruongPhong("Le Van D", 15000, "01/01/2025", 2000)

ctv.inThongTin()
nvct.inThongTin()
tp.inThongTin()
