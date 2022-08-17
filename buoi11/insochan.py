a = [8, 3, 5, 6, 7, 1, 2]
def chan1(mang):
    for i in mang:
        if i % 2 == 0:
            print(i)

chan1(a)

# Không được print trong hàm chan1, bạn phải làm sao?
def chan2(mang):
    kq = []
    for i in mang:
        if i % 2 == 0:
            kq.append(i)
    return kq

print(chan2(a))

def chan3(mang):
    for i in mang:
        if i % 2 == 0:
            yield i

print(list(chan3(a)))