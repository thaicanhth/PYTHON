n = open("input.txt")

n = int(input("Nhap n = "))
for i in range(2, n):
    if n % i == 0:
        print(n, "khong phai la so nguyen to")
        break
else:
    print(n, "la so nguyen to")