ho_ten = input("Nhap ho ten sinh vien: ")
s = input("Nhap tư can tim: ")

if s.capitalize() in ho_ten:
    print(s, "co trong ho va ten: ", ho_ten)
else:
    print(s, "Khong co trong ho va ten:", ho_ten)
