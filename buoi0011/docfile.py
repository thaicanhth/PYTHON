f = open("input.data", mode= "r", encoding="utf-8")

noi_dung = f.readlines()

print(noi_dung)

f.close()

print(noi_dung[1].strip())