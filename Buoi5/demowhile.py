n = int(input("Nhap n = "))

s = 0
i = 1
while i <= n:
    if i % 2 == 0:
        s += i
    i += 1
print("Tong cac so chan la:", s)
