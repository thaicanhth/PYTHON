# Viết chương trình nhập số nguyên dương n từ 0 đến 6. Sau đó in ra thứ trong tuần tương ứng:
# 0: Chủ Nhật; 1: Thứ Hai; 2: Thứ Ba; 3: Thứ Tư; 4: Thứ Năm; 5: Thứ Sáu; 6: Thứ Bảy.
# Nếu n ko hợp lệ (ko phải số nguyên dương trong khoảng từ 0 đến 6) thì in ra màn hình "F".
while(True):
    n = int(input("Mời bạn nhập số n: "))
    if (n == 0):
        print("Chủ Nhật")
    elif (n == 1):
        print("Thứ Hai")
    elif (n == 2):
        print("Thứ Ba")
    elif (n == 3):
        print("Thứ Tư")
    elif (n == 4):
        print("Thứ Năm")
    elif (n == 5):
        print("Thứ Sáu")
    elif (n == 6):
         print("Thứ Bảy")
    else:
        print("F")