#
# Example of working with funcitons
# 

# defining basic function

def func1():
    print("I am a function!")

# func1()

# function that takes in arguments

def func2(arg1, arg2):
    print(arg1, ", ", arg2)

def cube(x):
    return x*x*x

# func2("abc", "def")
# print(cube(3))
# print(func2("10", "20"))


# function with default argument

def power(x, n = 1):
    result = 1
    for i in range(n):
        result *= x
    return result

# print(power(2))
# print(power(2, 3))

# print(power(x=3, n=4))

# function with variable number of parameters
def multi_add(*args):
    result = 0;

    for i in args:
        result += i
    
    return result

print(multi_add(10,1, 4, 5, 6))