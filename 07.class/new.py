def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Cannot divide by zero"
        else:
            return self.num1 / self.num2
print("Add: ", add(2, 3))
print("Subtract: ", subtract(5, 3))
print("Multiply: ", multiply(2, 4))

my_calculator = Calculator(5, 2)
print("Add: ", my_calculator.add())
print("Subtract: ", my_calculator.subtract())
print("Multiply: ", my_calculator.multiply())
print("Divide: ", my_calculator.divide())