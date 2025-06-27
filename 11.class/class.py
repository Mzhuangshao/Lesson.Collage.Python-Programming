class Car:
    __wheels = 4
    def __drive(self):
        print("Driving...")
    def selfstate(self):
        print(self.__wheels)
        print(self.__drive())
    # def totalwheels(self):
    #     print("Total number of wheels in the car:", self.__wheels)
    #     self.__drive()
    def __init__(self,color):
        print("Creating a new car object...")
        print(color)
    def __del__(self):
        print("Deleting the car object...")
    
        
mycar = Car("red")
mycar.selfstate()