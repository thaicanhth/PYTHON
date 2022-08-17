from Demo5.nhanvien import NhanVien


class NVVP(NhanVien):
    def __init__(self, ho_ten="", so_nam_cong_tac=0, muc_luong=0, so_ngay_nghi=0):
        super().__init__(ho_ten, so_nam_cong_tac)
        self.muc_luong = muc_luong
        self.so_ngay_nghi = so_ngay_nghi

    def tinh_luong(self):
        return self.muc_luong - self.so_ngay_nghi * 10

    def __str__(self):
        return super().__str__() + f", Mức lương: {self.muc_luong}, " \
                                   f" Số ngày nghỉ: {self.so_ngay_nghi}, " \
                                   f" Lương: {self.tinh_luong()}"
