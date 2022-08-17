n = int(input("Nhap n = "))


def in_n(n):
    for i in range(1, n + 1):
        print("I love phython", i)

        f = lambda n: in_n(n)
        f(n)