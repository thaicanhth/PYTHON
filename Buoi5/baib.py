x = float(input("Nhap x = "))
n = int(input("Nhap n = "))

s = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        s +=x ** i
    else:
        s -= x ** i

print("Tong la", s)
