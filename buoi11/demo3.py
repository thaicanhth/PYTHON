c = ['a', 'F', 'b']


def f(s):
    s = str(s)
    return s.lower(), s.upper()


kq = map(f, c)
print(list(kq))
