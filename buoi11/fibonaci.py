n = int(input("Nhap n = "))

i = 0


def fibo(i):
    if i == 0 or i == 1:
        return i
    else:
        return fibo(i - 1) + fibo(i - 2)


kq = fibo(i)
while kq <= n:
    print(kq, " ", end=" ")
    i += 1
    kq = fibo(1)
