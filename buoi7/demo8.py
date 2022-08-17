s = input("Nhap chuoi: ")
x = input("Nhap vào 1 tư bat ky: ")

i = s.find(x)
if i < 0:
    print("Tu", x, "Thu nhi khong co trong chuoi: ", s)
else:
    i += len(x)
    i = s.find(x)
    if i < 0:
        print("Tu", x, "thu nhi co trong chuoi: ", s)
    else:
        print("vi tri cua tu", x, "thu nhi xuat hien là: ", i)
