a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
d = float(input("Nhap d: "))

min1 = min(a, b, c, d)

min2 = a
if min2 > b:
    min2 = b
if min2 > c:
    min2 = c
if min2 > d:
    min2 = d

print(min1, min2)