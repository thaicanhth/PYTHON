def hoc_luc(diem):
    if diem < 5:
        return "Yếu"
    elif diem < 7:
        return "Tbinh"
    elif diem < 8:
        return "Khá"
    elif diem < 9:
        return "Giỏi"
    else:
        return "XS"


class SinhVien:
    def __init__(self, ho_ten="", diem=0):
        # tao thuoc tinh
        self.ho_ten = ho_ten
        self.diem = diem

    # tao pthuc nhap
    def nhap(self):
        self.ho_ten = input("Nhập họ tên: ")
        self.diem = float(input("Nhập điểm: "))

    def xuat(self):
        print(f"Họ tên: {self.ho_ten}, Điểm: {self.diem}, Học lực: {hoc_luc(self.diem)}")


# main
sv1 = SinhVien()
sv1.nhap()
sv1.xuat()

sv2 = SinhVien("Tấn Đạt", 5.5)
sv2.xuat()
