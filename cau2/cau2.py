x = int(input("Nhập x: "))
y = int(input("Nhập y: "))


def luythua(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return luythua(x, y + 1) * float(1 / x)
    else:
        return x * luythua(x, y - 1)


print("Kq là:", luythua(x, y))
