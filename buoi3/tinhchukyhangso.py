import math

G = 9.8

chieu_dai = float(input("Nhap chieu dai con lac: "))

t = 2 * math.pi * math.sqrt(chieu_dai / G)

print("chu ky con lac:", t)
print("chu ky con lac = {:.1f}".format(t))
print("chu ky con lac %.1f" % t)