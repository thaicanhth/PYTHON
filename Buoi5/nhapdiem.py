while True:
    diem = float(input("Nhap diem: "))
    if 0 <= diem <= 10:  # diem >= 0 and diem <= 10:
        break
    print("Ban phai nhap diem tư 0 den 10")

print("Diem =", diem)
