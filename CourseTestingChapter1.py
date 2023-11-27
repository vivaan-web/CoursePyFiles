import random

#Ops with Numbers, and understand types, all variables are dynamic
a=50+50
print(a)
print(type(a))
b=20.3
print(b)
print(type(b))
print(a+b)

#Leveraging Print and Print formatting.
print("Hello")
print('World')
print("I'll come back")
print("\thello\n\tworld,\n\tstring modifiers have been used")
print("the previous 3 lines had this many letters (indents count as 2 letters, newlines count as 2 letters): "+str(len("hello\n\tworld,\n\tstring modifiers have been used")))
print(f"I love how '2'+'3'=23 and 2+3=5 in Python \nExample: 2+3:{2+3} \nand \t'2'+'3':{'2'+'3'}")
#learning Additional string and print operations and formatting.
for i in range(1):print('ab\n'+' cd\n'+'  ef\n'+'   gh\n')
print('hello World'[0:2]*8)
print("Splitting Strings To Lists!".split(" "))

#Print and string formatting. Includes f-strings, lists, and the random mudle
names=["Ben","Benny","Benjamin","Benjamin Franklin"]
randvar=int(random.randint(0,3))
print(f"Here's a name from a list: {names[randvar]}")

# Comparison Ops
print(5 > 3)  # Output: True
print(5 >= 3)  # Output: True
print(5 < 3)  # Output: False
print(5 <= 3)  # Output: False
print(5 == 3)  # Output: False
print(5 != 3)  # Output: True

# Lists
numbers = [1, 2, 3, 4, 5]

# For loop
for num in numbers:
    print(num)  # Output: 1, 2, 3, 4, 5

# While loop
i = 0
while i < len(numbers):
    print(numbers[i])  # Output: 1, 2, 3, 4, 5
    i += 1

# Useful operators
print(2 + 3)  # Output: 5
print(5 - 2)  # Output: 3
print(4 * 3)  # Output: 12
print(10 / 2)  # Output: 5.0

# Lists
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: orange

# Tuples
colors = ("red", "green", "blue")
print(colors[1])  # Output: green
print(colors.count("red"))  # Output: 1

# Dictionaries
student = {"name": "John", "age": 30, "city": "New York"}
print(student["name"])  # Output: John
print(student.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(student.values())  # Output: dict_values(['John', 30, 'New York'])

# Functions
def greet(name):
    print("Hello,", name)

greet("Alice")  # Output: Hello, Alice

# Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Bob", 25)
print(person.name)  # Output: Bob
print(person.age)  # Output: 25

# OOP
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!", self.name)

dog = Dog("Charlie", "Golden Retriever")
dog.bark()  # Output: Woof! Charlie

# Errors and exception handling
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    
def hello(name):
    print(f'Hello {name}')
    def greet():
        return '\t This is the greet() func inside hello!'
    def welcome():
        return '\t This is welcome() inside hello'
    print(greet())
    print(welcome())
    print('This is the end of the hello function!')
hello('Vivaan')

def FuncRunner(func):
    print("Just mediating another function")
    print(func())
    
def test():
    return 'Testing Functions as arguments'

FuncRunner(test)

def new_decorator(originalFunction):
    def wrap_func():
        print("Code here, will execue before the func")
        originalFunction()
        print("Code here will execute after the func()")
    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")
    
decorated_func=new_decorator(func_needs_decorator)
decorated_func()

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3
print(list(gencubes(10)))

def gen_fibon(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b
    
print(list(gen_fibon(20)))

def simple_gen():
    for x in range(3):
        yield x
for number in simple_gen():
    print(number)
g=simple_gen()

s='hello'

from PIL import Image

mac = Image.open('example.jpg')
mac.show()
print(mac.size)
mac.paste(im=mac.crop((20,20,172,178)),box=(0,0))
mac.show()

