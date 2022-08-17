import sys

# tao biến chứa danh sách các nhân viên
from Demo5.nhanviensanxuat import NVSX
from Demo5.nhanvienvanphong import NVVP

dsnv = []


def load_ds():
    f = open("input.txt", mode="r", encoding="utf-8")

    data_file = f.readlines()

    for row in data_file:
        row_list = row.split("-")
        if row_list[0] == "S":
            # dòng này là nv sản xuất
            nvsx = NVSX(row_list[1], int(row_list[2]), int(row_list[3]))
            dsnv.append(nvsx)
        else:
            nvvp = NVVP(row_list[1], int(row_list[2]), int(row_list[3]), int(row_list[4]))
            dsnv.append(nvvp)

    f.close()
    print("Đã load xong dữ liệu")


def tong_tien():
    tong = 0
    for nv in dsnv:
        tong += nv.tinh_luong() + nv.phu_cap

    print("Tổng số tiền cần trả là:", tong)

def ghi_thong_tin():
    f = open("nhanvien.txt", mode="w", encoding="utf-8")

    for nv in dsnv:
        if nv.so_nam_cong_tac > 7:
            f.write(nv.__str__())

    f.close()
    print("Đã ghi xong")


def xuat_thong_tin():
    print("Danh sách tất cả các nhân viên:")
    for nv in dsnv:
        print(nv)


def menu():
    while True:
        print("1. Load danh sách nhân viên từ file")
        print("2. Tổng số tiền công ty cần trả")
        print("3. Ghi thông tin nv có số năm công tác > 7 ra file")
        print("4. Xuất thông tin tất cả nhân viên ra màn hình")
        print("5. Thoát chương trình")

        chon = int(input("Mời bạn chọn chức năng: "))

        if chon == 1:
            load_ds()
        elif chon == 2:
            tong_tien()
        elif chon == 3:
            ghi_thong_tin()
        elif chon == 4:
            xuat_thong_tin()
        elif chon == 5:
            print("Tạm biệt, hẹn gặp lại")
            break
            # return
            # sys.exit(0)
        else:
            print("Bạn chọn sai, mời chọn lại")


# main
menu()