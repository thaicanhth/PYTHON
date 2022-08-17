def in_so_chan(*num):
    for i in num:
        if i % 2 == 0:
            print(i, end=" ")

in_so_chan(2, 5, 7, 8)