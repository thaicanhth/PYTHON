def hoc_luc(diem):
    if diem < 3:
        return "kem"
    elif diem < 4:
        return "Yếu"
    elif diem < 6:
        return "Tbinh"
    elif diem < 8:
        return "Khá"
    elif diem < 10:
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

    def __gt__(self, other):
        if self.diem > other.diem:
            return True
        else:
            return False

    def __str__(self):
        return f"Họ tên: {self.ho_ten}, Điểm: {self.diem}, Học lực: {hoc_luc(self.diem)}"

# main
sv1 = SinhVien()
sv1.nhap()
sv1.xuat()

sv2 = SinhVien("Tấn Đạt", 5.5)
sv2.xuat()

# print("So sánh 2 sv:")
# if sv1 > sv2:
#     print(sv1)
# else:
#     print(sv2)
