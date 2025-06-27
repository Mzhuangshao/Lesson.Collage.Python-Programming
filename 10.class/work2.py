import math
class Circle:
    # pai = 3.14
    def get_perimeter(self, radius):
        return 2 * math.pi * radius
    def get_area(self, radius):
        return math.pi * radius ** 2


c = Circle()
print(c.get_perimeter(8))
print(c.get_area(2))