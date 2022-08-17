ani = {"name2": "Tom", "name1": "Jerry", "name3": "Dog"}
ani_sort = sorted(ani.items(), key=lambda y: y[1])
print(ani_sort)
