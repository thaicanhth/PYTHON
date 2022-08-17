class Person:
    def __init__(self, name="", age=0):
        self.__name = name  # __name là thuộc tính private
        self.__age = age

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    # thuộc tính ảo cho __name
    name = property(get_name, set_name)


    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    # thuộc tính ảo cho __age
    age = property(get_age, set_age)

p1 = Person("Na", 19)
print(p1)
# p1.set_name("Ly Na")
# print(p1)
p1.name = "Ly Na"
print(p1)
