from Demo5.nhanvien import NhanVien


class NVSX(NhanVien):
    def __init__(self, ho_ten="", so_nam_cong_tac=0, so_san_pham=0):
        super().__init__(ho_ten, so_nam_cong_tac)
        self.so_san_pham = so_san_pham

    def tinh_luong(self):
        return self.so_san_pham * 10

    def __str__(self):
        return super().__str__() + f", Số sản phẩm: {self.so_san_pham}," \
                                             f" Lương: {self.tinh_luong()}"