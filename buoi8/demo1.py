s = input("Nhap chuoi: ")
x = input("Nhap tu can tim: ")

i = s.find(x)
if i < 0:
    print(x, "Khong co trong chuoi")
else:
   i = s.find(x, i + len(x))
   if i < 0:
       print("Tu", x, "thu nhi khong co trong chuoi")
   else:
       print("vi tri cua tu", x, "thu nhi la:", i)