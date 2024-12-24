# functions to be tested

# calculate the mean of two numbers
def my_mean(x, y):
    return (x + y) / 2

# calculate the quotient of two numbers
def my_divide(x, y):
    if y == 0:
        raise ValueError('Division By Zero')
    return x / y

# OOP Example
class student:
    def __init__(self, name, grade, program):
        self.name = name
        self.grade = grade
        self.program = program

    def age(grade):
        return 17 + grade