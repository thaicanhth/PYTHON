a = float(input("Nhap vao a:"))
b = float(input("Nhap vao b"))
if a == 0:
    if b == 0:
        print("pt vo so nghiem")
    else:
        print("Vo nghiem")
else:
    print("Pt co nghiem:", -b / a)