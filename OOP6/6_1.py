from abc import ABC, abstractmethod

# Custom Exception
class GiaKhongHopLe(Exception):
    pass

class HangHoa(ABC):
    def __init__(self, ten, gia):
        if gia < 0:
            raise GiaKhongHopLe("Giá không hợp lệ!")
        self._ten = ten
        self._gia = gia

    @property
    def ten(self):
        return self._ten

    @property
    def gia(self):
        return self._gia

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self.ten} - Giá: {self.gia}"

    def __eq__(self, other):
        return self.gia == other.gia

    def __lt__(self, other):
        return self.gia < other.gia


class HangDienMay(HangHoa):
    def __init__(self, ten, gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(ten, gia)
        self.bao_hanh = bao_hanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def mo_ta(self):
        return f"{self.ten} (Điện máy) - Giá: {self.gia}, BH: {self.bao_hanh} tháng, {self.dien_ap}V, {self.cong_suat}W"


class HangSanhSu(HangHoa):
    def __init__(self, ten, gia, nguyen_lieu):
        super().__init__(ten, gia)
        self.nguyen_lieu = nguyen_lieu

    def mo_ta(self):
        return f"{self.ten} (Sành sứ) - Giá: {self.gia}, Nguyên liệu: {self.nguyen_lieu}"


class HangThucPham(HangHoa):
    def __init__(self, ten, gia, nsx, hsd):
        super().__init__(ten, gia)
        self.nsx = nsx
        self.hsd = hsd

    def mo_ta(self):
        return f"{self.ten} (Thực phẩm) - Giá: {self.gia}, NSX: {self.nsx}, HSD: {self.hsd}"


# Ví dụ sử dụng
ds = [
    HangDienMay("Máy giặt", 5000000, 24, 220, 2000),
    HangSanhSu("Bát gốm", 100000, "Gốm sứ"),
    HangThucPham("Sữa tươi", 30000, "01/04/2026", "01/05/2026")
]

for h in ds:
    print(h.mo_ta())
