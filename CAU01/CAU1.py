a = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]
b = []
c= []
for i in range(len(a)-1):
    b.append(a.count(a[i]))

for i in range(len(b)-1):
    if b[i] == max(b):
        c.append(a[i])

print(c[0])