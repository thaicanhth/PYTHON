print("=========MENU=========")
print("1. in cac so nguyen to tu 2 den n")
print("2. in cac so hoan thien tu 2 den n")
print("3. thoat")
chon = int(input("Moi ban chon"))
if chon == 1:
    n = int(input("Nhap a = "))
    for m in range(2, n + 1):
        for i in range(2, m):
            if m % i == 0:
                break
            else:
                print(m, end=" ")

