from cau3.nguoi import Nguoi


class GiaoVien(Nguoi):
    def __init__(self, ma_so="", ho_ten="", que_quan="", nam_sinh=0, bai_bao=0):
        super().__init__(ma_so, ho_ten, que_quan, nam_sinh)
        self.__bai_bao = bai_bao

    def __str__(self):
        return super().__str__() + f", Số năm: {self.__bai_bao}\n"

    def get_bai_bao(self):
        return self.__bai_bao

    def set_bai_bao(self, x):
        if x > 0:
            self.__bai_bao = x

    so_nam = property(get_bai_bao, set_bai_bao)


    def khen_thuong(self):
        if self.__bai_bao > 2:
            return True
        else:
            return False