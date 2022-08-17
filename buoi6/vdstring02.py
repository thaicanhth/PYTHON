s = input("Nhap chuoi: ")
n = len(s)
mid = (int(n / 2))
print("nua chuoi ben trái", s[:mid])
print("nua chuoi ben phải", s[mid])

print("nua chuoi ben trái", s[:(int(len(s) / 2))])
print("nua chuoi ben trái", s[:(int(len(s) / 2)):])