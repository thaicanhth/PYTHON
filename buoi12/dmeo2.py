import sys


class Music:
    def __init__(self, ten="", bai_hat_thich="", bai_hat_khong_thich=""):
        self.ten = ten
        self.bai_hat_thich = bai_hat_thich
        self.bai_hat_khong_thich = bai_hat_khong_thich

    def listen(self, bh, kieu):
        if kieu:
            print(f"{self.ten} đang nghe bài hát {bh} và rất thích nó")
        else:
            print(f"{self.ten} đang nghe bài hát {bh} nhưng không thích nó")


music_list = []


def tao_danh_sach():
    while True:
        ten = input("Nhập tên người nghe: ")
        bht = input("Nhập tên bài hát yêu thích: ")
        bhkt = input("Nhập tên bài hát không thích: ")

        obj = Music(ten, bht, bhkt)

        music_list.append(obj)

        tiep = input("Bạn có nhập nữa không (C/K): ")

        if tiep.upper() == "K":
            break


def tim_bai_hat():
    bai_hat = input("Nhập tên bài hát cần tìm: ")

    for bh in music_list:
        if bai_hat == bh.bai_hat_thich:
            bh.listen(bai_hat, True)
        elif bai_hat == bh.bai_hat_khong_thich:
            bh.listen(bai_hat, False)


def menu():
    while True:
        print("1. Tạo danh sách")
        print("2. Tìm bài hát")
        print("3. Thoát")

        chon = int(input("Bạn chọn mục nào: "))
        if chon == 1:
            tao_danh_sach()
        elif chon == 2:
            tim_bai_hat()
        elif chon == 3:
            sys.exit(0)
        else:
            print("Bạn chọn sai, hãy chọn lại")


# main
menu()
