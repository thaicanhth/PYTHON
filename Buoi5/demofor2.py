n = int(input("Nhap n = "))
s = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        s += i

print("Tong cac so chan la:", s)
# cach 2
s = 0
for i in range(0, n + 1, 2):
    print(i)
    s += i
print("Tong cac so chan la:", s)
# cach 3
s = sum(list(range(0, n + 1, 2)))
print("Tong cac so chan la:", s)
