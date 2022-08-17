fullname = ("Nhap Họ va Ten")

i = fullname.find("")
if i < 0:
    print("Khong the lấy duoc ho cua sinh vien")
else:
    ho = fullname[:i]
    print("ho cua sinh viên: ", ho)
