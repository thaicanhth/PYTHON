from cau3.nguoi import Nguoi


class NVSX(Nguoi):
    def __init__(self, ma_so="", ho_ten="", que_quan="", nam_sinh=0, san_kien=0):
        super().__init__(ma_so, ho_ten, que_quan, nam_sinh)
        self.__san_kien = san_kien

    def __str__(self):
        return super().__str__() + f", San kien: {self.__san_kien}\n"

    def get_san_kien(self):
        return self.__san_kien

    def set_san_kien(self, x):
        if x > 0:
            self.__san_kien = x

    san_kien = property(get_san_kien, set_san_kien)


    def khen_thuong(self):
        if self.__san_kien:
            return True
        else:
            return False