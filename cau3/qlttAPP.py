ds = []  # danh sách các cầu thủ và phục vụ

def chuc_nang_1():
    while True:
        chon = int(input("Bạn chọn nhập can bo (1) hay giao vien (2): "))
        # nhập thông tin chung
        ma_so = input("Nhập mã số: ")
        ho_ten = input("Nhập họ tên: ")
        que_quan = input("Nhập quê quán: ")
        nam_sinh = int(input("Nhập năm sinh: "))

        if chon == 1:
            # nhập CanBo
            san_ken = int(input("Nhập số thành tích: "))
            ct = CanBo(ma_so, ho_ten, que_quan, nam_sinh, san_ken)
            ds.append(ct)

        else:
            # nhập GiaoVien
            bai_bao = int(input("Nhập số năm: "))
            pv = GiaoVien(ma_so, ho_ten, que_quan, nam_sinh, bai_bao)
            ds.append(pv)

        tiep = input("Bạn có nhập nữa không? (C/K): ")
        if tiep.upper() == "K":
            break

def chuc_nang_3():
    for x in ds:
        if x.khen_thuong():
            print(x)


def chuc_nang_4():
    ma = input("Nhập mã cần tìm: ")
    for x in ds:
        if x.ma_so.upper() == ma.upper():
            print(x)
            break
    else:
        print("Không tìm thấy")

from cau3.CanBo import NVSX
from Demo5.nhanvienvanphong import NVVP


def chuc_nang_5():
    ma = input("Nhập mã cần tìm: ")
    for i in range(0, len(ds)):
        if ds[i].ma_so.upper() == ma.upper():
            # sửa  ds[i]
            ds[i].ho_ten = input("Nhập họ tên: ")
            ds[i].que_quan = input("Nhập quê quán: ")
            ds[i].nam_sinh = int(input("Nhập năm sinh: "))

            if isinstance(ds[i], CanBo):
                ds[i].san_kien = int(input("Nhập san kien: "))
            else:
                ds[i].bai_bao = int(input("Nhập bai bao: "))

            break
    else:
        print("Không tìm thấy")


def chuc_nang_7():
    for x in ds:
        if isinstance(x, CanBo):
            if x.bai_bao() == False:
                print(x)


def menu():
    while True:
        print("1. Nhập vào danh sách cầu thủ và phục vụ\n"
              "3. In ra man hinh danh sach can bo, giao vien được khen thương\n"
              "4. Tìm và in ra màn hinh thông tin cua can bộ, giao vien co ma duoc nhap tu ban phim\n"
              "5. Tìm và sửa thông tin của can bo, giao vien có mã ma được nhập từ bàn phím\n"
              "7. In ra danh sách các giao vien không co bai bao\n"
              "10. Thoát")

        chon = int(input("Mời bạn chọn chức năng: "))
        if chon == 1:
            chuc_nang_1()
        elif chon == 3:
            chuc_nang_3()
        elif chon == 4:
            chuc_nang_4()
        elif chon == 5:
            chuc_nang_5()
        elif chon == 7:
            chuc_nang_7()
        elif chon == 10:
            break
        else:
            print("Bạn chọn sai, mời chọn lại")

# main
menu()