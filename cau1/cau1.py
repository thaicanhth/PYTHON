n = int(input("Nhập số nguyên dương: "))

t = 0
d = 0

def check(x):
    if i % 2 == 0 and i % 3 == 0:
        return True
    else:
        return False

for i in range(2, n + 1):
    if check(i):
        t += i
        d += 1

if d == 0:
    print("Không thể tính được")
else:
    print("TBC các số chẵn chia hết cho 3 là:", t / d)