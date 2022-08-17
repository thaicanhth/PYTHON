n = int(input("Nhap n = "))
for i in range(1, n + 1):
    m = int(input("Nhap so duong"))
    if m < 0:
        break
else:
    print("Da nhap xong", n, "so duong")
i = 1
# cach 2 dung lenh while
while i <= n:
    m = int(input("Nhap so duong"))
    if m < 0:
        break
else:
    print("Da nhap xong", n, "so duong")
# viết chương trình nhập n số dương. chương trình sẽ kết thúc nếu nhập số âm
