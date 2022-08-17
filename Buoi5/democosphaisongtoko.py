n = int(input("Nhap n = "))
for i in range(2, n):
    if n % i == 0:
        print(n, "khong phai la so nguyen to")
        break
else:
    print(n, "la so nguyen to")
# cach2 bằng lệnh while
i = 2
while i < n:
    if n % i == 0:
        print(n, "khong phai la so nguyen to")
        break
else:
    print(n, "la so nguyen to")
