n = int(input("Nhap n = "))
s = 0
for i in range(1, n):
        if n % i == 0:
            s += i

if n == s:
    print(n, "la so hoan thien")
else:
    print(n, "khong phai la so hoan thien")

