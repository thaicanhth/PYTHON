def menu():
    while True:
        print("1. Tinh tong\n"
              "2. Tinh hieu\n"
              "3. Tinh tich\n"
              "4. Tinh thuong\n"
              "5. Tinh luy thua\n"
              "6. Tinh chuong trinh\n")
        chon = int(input("Mời bạn chọn: "))
        if chon < 1 or chon > 6:
            print("Bạn chọn sai chức năng")
        else:
            if chon == 1:
                tinh_tong()
            elif chon == 2:
                tinh_hieu()
            elif chon == 3:
                tinh_tich()

            elif chon == 4:
                tinh_thuong()
            elif chon == 5:
                tinh_luy_thua()
            else:
                print("Tạm biệt")
                sys.exit(0)  # Thoát chương trình

                import sys

                def tinh_tong():
                    print(f"Tổng của {a} và {b} là {a + b}")

                def tinh_hieu():
                    print(f"Hiệu của {a} và {b} là {a - b}")

                def tinh_tich():
                    print(f"Tích của {a} và {b} là {a * b}")

                def tinh_thuong():
                    if b != 0:
                        print(f"Thương của {a} và {b} là {a / b}")
                    else:
                        print("Không thể thực hiện phép chia")

                def tinh_luy_thua():
                    print(f"Lũy thừa của {a} mũ {b} là {a ** b}")


a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
menu()
