class NhanVien:
    def __init__(self, ho_ten="", so_nam_cong_tac=0):
        self.ho_ten = ho_ten
        self.so_nam_cong_tac = so_nam_cong_tac

    @property
    def phu_cap(self):
        return 100 + (self.so_nam_cong_tac - 1) * 20

    def tinh_luong(self):
        pass

    def __str__(self):
        return f"Họ tên: {self.ho_ten}, " \
               f"Số năm công tác: {self.so_nam_cong_tac}, " \
               f"Phụ cấp: {self.phu_cap}"
