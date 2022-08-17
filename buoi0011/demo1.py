f = open("input.txt")

s = f.read().split(",")

tong = 0
for i in s:
    tong += float(i)

    f.close()
    f1 = open("input.txt", "w", encoding="utf-8")
    f1.write("tong la: " + str(tong))
    f1.close()
