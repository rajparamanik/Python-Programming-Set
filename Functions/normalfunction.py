#this is a normal function
def add(a, b):
    return a + b    

print(add(5, 10))


#this is a normal function with default parameters
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))


#this is a normal function with variable-length arguments
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply(2, 3, 4))   


#this is a normal function with keyword arguments
def introduce(name, age, city):
    return f"My name is {name}, I am {age} years old and I live in {city}."
print(introduce(name="Charlie", age=25, city="New York"))


#this is a normal function with a return statement
def square(num):
    return num ** 2
print(square(5))
