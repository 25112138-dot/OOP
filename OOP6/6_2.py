from abc import ABC, abstractmethod

# Custom Exceptions
class TuoiKhongHopLe(Exception):
    pass

class BacKhongHopLe(Exception):
    pass


class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        if not (18 <= tuoi <= 65):
            raise TuoiKhongHopLe("Tuổi phải từ 18 đến 65")
        self._ho_ten = ho_ten
        self._tuoi = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi

    @property
    def tuoi(self):
        return self._tuoi

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self._ho_ten}, {self._tuoi} tuổi, {self._gioi_tinh}, {self._dia_chi}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._ho_ten == other._ho_ten

    def __lt__(self, other):
        return self._ho_ten < other._ho_ten


class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        if not (1 <= bac <= 10):
            raise BacKhongHopLe("Bậc công nhân phải từ 1–10")
        self.bac = bac

    def mo_ta(self):
        return f"Công nhân {self._ho_ten}, bậc {self.bac}"


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh

    def mo_ta(self):
        return f"Kỹ sư {self._ho_ten}, ngành {self.nganh}"


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"Nhân viên {self._ho_ten}, công việc {self.cong_viec}"


# Quản lý danh sách cán bộ với with statement
class QLCB:
    def __init__(self):
        self.ds = []

    def themMoi(self, cb):
        self.ds.append(cb)

    def hienThi(self):
        for cb in self.ds:
            print(cb.mo_ta())

    def luuFile(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for cb in self.ds:
                f.write(str(cb) + "\n")

    def docFile(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())


# Ví dụ sử dụng
ql = QLCB()
ql.themMoi(CongNhan("Nguyen Van Hieu", 30, "Nam", "Hà Nội", 5))
ql.themMoi(KySu("Tran Thi Dung", 40, "Nữ", "Hà Nội", "Cơ khí"))
ql.themMoi(NhanVien("Le Van Minh", 28, "Nam", "Hà Nội", "Văn thư"))

ql.hienThi()
ql.luuFile("canbo.txt")
ql.docFile("canbo.txt")
