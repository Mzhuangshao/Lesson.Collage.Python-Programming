class Car:
    weels = 4
    set = 5
    def drive(self,peoples):
        print("Driving with", peoples, "people")

my_car = Car()
my_car1 = Car()

my_car.weels =2
print(my_car.weels)
print(my_car1.weels)
print(my_car.drive(3))