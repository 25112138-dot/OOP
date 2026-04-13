import math

# Custom Exception
class MauSoBangKhong(Exception):
    pass

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise MauSoBangKhong("Mẫu số không được bằng 0!")
        self.__tu = tu
        self.__mau = mau

    @property
    def tu(self):
        return self.__tu

    @property
    def mau(self):
        return self.__mau

    # Hiển thị
    def __str__(self):
        if self.__mau == 1:
            return str(self.__tu)
        return f"{self.__tu}/{self.__mau}"

    def __repr__(self):
        return self.__str__()

    # Toán tử cộng
    def __add__(self, other):
        tu = self.__tu * other.mau + other.tu * self.__mau
        mau = self.__mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    # Toán tử trừ
    def __sub__(self, other):
        tu = self.__tu * other.mau - other.tu * self.__mau
        mau = self.__mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    # Toán tử nhân
    def __mul__(self, other):
        tu = self.__tu * other.tu
        mau = self.__mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    # Toán tử chia
    def __truediv__(self, other):
        tu = self.__tu * other.mau
        mau = self.__mau * other.tu
        return PhanSo(tu, mau).toi_gian()

    # Kiểm tra tối giản
    def is_toi_gian(self):
        return math.gcd(self.__tu, self.__mau) == 1

    # Trả về phân số tối giản
    def toi_gian(self):
        gcd = math.gcd(self.__tu, self.__mau)
        return PhanSo(self.__tu // gcd, self.__mau // gcd)

    # So sánh
    def __eq__(self, other):
        return self.__tu * other.mau == other.tu * self.__mau

    def __lt__(self, other):
        return self.__tu * other.mau < other.tu * self.__mau

    def __gt__(self, other):
        return self.__tu * other.mau > other.tu * self.__mau
