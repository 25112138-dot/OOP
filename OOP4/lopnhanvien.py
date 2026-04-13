class NhanVien:
    def __init__(self, ma_nv, ten_nv, luong_co_ban, he_so):
        self.__ma_nv = ma_nv          # private
        self.__ten_nv = ten_nv        # private
        self.__luong_co_ban = luong_co_ban
        self.__he_so = he_so

    # Getter & Setter
    def get_ma_nv(self):
        return self.__ma_nv

    def set_ma_nv(self, ma_nv):
        self.__ma_nv = ma_nv

    def get_ten_nv(self):
        return self.__ten_nv

    def set_ten_nv(self, ten_nv):
        self.__ten_nv = ten_nv

    def get_luong_co_ban(self):
        return self.__luong_co_ban

    def set_luong_co_ban(self, luong):
        self.__luong_co_ban = luong

    def get_he_so(self):
        return self.__he_so

    def set_he_so(self, he_so):
        self.__he_so = he_so

    # Phương thức tính lương
    def tinhLuong(self):
        return self.__luong_co_ban * self.__he_so

    # Phương thức in thông tin
    def inTTin(self):
        print(f"Mã NV: {self.__ma_nv}, Tên: {self.__ten_nv}, "
              f"Lương: {self.tinhLuong()}")

    # Phương thức tăng lương
    def tangLuong(self, ti_le):
        self.__luong_co_ban *= (1 + ti_le)


# Ví dụ sử dụng
nv1 = NhanVien("NV01", "Nguyen Van Minh", 5000, 2.5)
nv1.inTTin()
nv1.tangLuong(0.1)
nv1.inTTin()
