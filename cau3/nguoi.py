class Nguoi:
    def __init__(self, ma_so="", ho_ten="", que_quan="", nam_sinh=0):
        self.__ma_so = ma_so
        self.__ho_ten = ho_ten
        self.__que_quan = que_quan
        self.__nam_sinh = nam_sinh

    def __str__(self):
        return f"Mã số: {self.__ma_so}, Họ tên: {self.__ho_ten}, Quê quán: {self.__que_quan}, Năm sinh: {self.__nam_sinh}"

    def khen_thuong(self):
        pass

    def get_ma_so(self):
        return self.__ma_so

    def set_ma_so(self, x):
        self.__ma_so = x

    def get_ho_ten(self):
        return self.__ho_ten

    def set_ho_ten(self, x):
        self.__ho_ten = x

    def get_que_quan(self):
        return self.__que_quan

    def set_que_quan(self, x):
        self.__que_quan = x

    def get_nam_sinh(self):
        return self.__nam_sinh

    def set_nam_sinh(self, x):
        if x > 0:
            self.__nam_sinh = x

    ma_so = property(get_ma_so, set_ma_so)
    ho_ten = property(get_ho_ten, set_ho_ten)
    que_quan = property(get_que_quan, set_que_quan)
    nam_sinh = property(get_nam_sinh, set_nam_sinh)