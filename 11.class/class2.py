class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 1
    def set_age(self, input_age):
        if 0 <= input_age <= 120:
            self.__age = input_age
    def get_age(self):
        return self.__age

class China(Person):
    def aa(self):
        print("aa")
class Chinese(Person,China):
    pass

# person = Person("Mar")

# person.set_age(25)
# age1 = person.get_age()
# print(age1)

CP = Chinese()
CP.aa()
age1 = China.get_age()
print(age1)