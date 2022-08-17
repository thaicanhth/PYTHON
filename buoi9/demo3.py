a = [i for i in range(1, int(input("Nhap n = ")) + 1) if i % 2 == 0]
print(a)
b = []
for i in range(0, len(a)):
    if i % 2 == 0:
        b.append(a[i])

print(b)
