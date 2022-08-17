class NhanVien:
    def __init__(self, first="", last=""):
        self.first = first
        self.last = last

    # tao thuoc tính fullname với @property
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, value):
        print("Đã gán được")
        self.first = value[:value.find(" ")]
        self.last = value[value.find(" ") + 1:]


nv1 = NhanVien("Chí", "Phèo")
print(nv1.fullname)

nv1.fullname = "Thị Nở"
print(nv1.fullname)
