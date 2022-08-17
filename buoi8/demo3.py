import getpass

password = getpass.getpass("nhap vao mk: ")
word = input("Nhap vao mk: ")
if len(password) >= 6 and password.isalnum():
    print("mk hop le")
else:
    print("mk khong hop le")
