s = input("nhập dãy sô cách nhau dấu phải: ").split(',')
s1 = set(s)
dem = 0
for i in s1:
    n = int(i.strip())
    #kiểm tra n có phải so ng to hay ko
    for j in range(2, n):
        if n % j == 0:
            break
        else:
            dem += 1
            print(f"có {dem} so ng to khac nhau")
