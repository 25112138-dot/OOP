class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def show(self):
        print(f"Tên: {self.ten}, Vũ khí: {self.vu_khi}, Màu sắc: {self.mau_sac}")

# Khởi tạo 2 đối tượng
sn1 = SieuNhan("Red", "Kiếm", "Đỏ")
sn2 = SieuNhan("Blue", "Súng", "Xanh")

sn1.show()
sn2.show()