class CanBo:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def inThongTin(self):
        print(f"Tên: {self.ten}, Tuổi: {self.tuoi}")


class CongNhan(CanBo):
    def __init__(self, ten, tuoi, bac):
        super().__init__(ten, tuoi)
        self.bac = bac

    def inThongTin(self):
        super().inThongTin()
        print(f"Bậc: {self.bac}")


class KySu(CanBo):
    def __init__(self, ten, tuoi, nganh):
        super().__init__(ten, tuoi)
        self.nganh = nganh

    def inThongTin(self):
        super().inThongTin()
        print(f"Ngành đào tạo: {self.nganh}")


class NhanVien(CanBo):
    def __init__(self, ten, tuoi, cong_viec):
        super().__init__(ten, tuoi)
        self.cong_viec = cong_viec

    def inThongTin(self):
        super().inThongTin()
        print(f"Công việc: {self.cong_viec}")


class QLCB:
    def __init__(self):
        self.ds = []

    def themMoi(self, cb):
        self.ds.append(cb)

    def timKiem(self, ten):
        for cb in self.ds:
            if cb.ten == ten:
                cb.inThongTin()
                return
        print("Không tìm thấy cán bộ")

    def hienThi(self):
        for cb in self.ds:
            cb.inThongTin()


# Ví dụ sử dụng
ql = QLCB()
ql.themMoi(CongNhan("Nguyen Van E", 30, 5))
ql.themMoi(KySu("Tran Van F", 35, "Cơ khí"))
ql.themMoi(NhanVien("Le Thi G", 28, "Văn thư"))

ql.hienThi()
ql.timKiem("Tran Van F")
