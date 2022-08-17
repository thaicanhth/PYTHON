a = [1, 2, 3]
a.extend([5, 7])
print(a)

a.extend([[8, 9], 7])
b = []
for i in a:
    if isinstance(i, list):
        b.extend(i)
    else:
        b.extend([i])
        #b.append(i)

print(b)

