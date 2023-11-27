import time
import math

#Single Line Comments
'''
Multiline Comments

Also in Python, all code is reliant on indentation. Code blocks are all ran because of indentation.
'''
#print(object*,sep,end,file)

print("Greetings","Traveler",sep="funifunifuni",end="\t")

print("Well,","Hello","There", sep="funni")

fd=open('output.txt','w')
print("String to be written to the file", fd)

var="Hello World"
var1="H"

print(var,var1,sep="\n")
print(type(fd))

a=123
b=0b100
c=0o234
d=0x435
e=23.45
f=True
g=False
h=5+6j
i=None
j=["Mercedes","BMW","Toyota","Honda","Hyundai","Rolls Royce","Volkswagen"]
k={"Apple":"Red", "Orange":"Orange","Banana":"Yellow"}
l=time
print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)
print(type(e),e)
print(type(f),f)
print(type(g),g)
print(type(h),h)
print(type(i),i)
print(type(j),j)
print(type(k),k)
print(type(l),l)
def printtype(data):
    print(type(data),data)
printtype(printtype)
class example():
    def __init__(main):
        pass
    def example(a):
        return a.split("b")
printtype(example)
printtype(__name__)
printtype(example.example)
printtype(2/3)
printtype(0.1+0.2)
print(1 is 1)
print(1 == 2)
print(100/5)
print(100//5)
print(math.pow(1,2))
print(1**2)
print(1^2)
print(2*3/5)
#left-to-right for arithmetic ops
print(1+2*6)

Err="fakevar"
del(Err)
#print(Err) if you try to print the deleted variable, an error is thrown

'''
user=input("Red pill, or blue pll?")
if("blue" in user): print("Nice choice! You lived!")
if "red" in user: 
    print("Great choice! You died!")
'''

for i in range(1,5):   
    for i in "FUNNY":
        print(i)

j=1
for i in range(1,11):
        print(i*j,i*(j+2),i*(j+3),i*(j+4),i*(j+5),i*(j+6),i*(j+7),i*(j+8),i*(j+9), sep="  ", end="\n ")

j=0x1111111111111111111111111111
print(j)
#for i in range(1,j):
    #print("Hello",i)
#wait until 7719472615821079694904732333912527190217998977709370935963838933860875309329

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Developer(Employee):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def developer_details(self):
        super().details()
        print(f"Language: {self.language}")
        
d=Developer("Vivaan",13,"CSharp")

class Animal:
    def eat(self):
        print("Eats")

class Dog(Animal):
    def bark(self):
        print("Barks")
        
class puppy(Dog):
    def weeps(self):
        print("weeps")
        
p=puppy()
p.bark()
p.eat()
p.weeps()

class Academic:
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

class Sports:
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

class Student_marks(Academic, Sports):
    def __init__(self, academic_score, sports_score):
        self.academic_score = academic_score
        self.sports_score = sports_score

    def aggregate(self):
        return float((self.sports_score + (self.academic_score * 4)) / 5)

s = Student_marks(96.53, 83.49)
print(s.aggregate())
print("The function for this aggregate grade came from this equation ((sports_grade + (academics_grade*4))/5)")
print("Essentially academics makes 80% of ones grade and sports include 20% of ones grade")
print("Although slightly unrealistic, this example demonstrates use of functions, classes and equations in Python")

class Employee2:
    def __init__(self, name, id_number, hourly_rate):
        self.name = name
        self.id_number = id_number
        self.hourly_rate = hourly_rate

    def get_name(self):
        return self.name

    def get_id_number(self):
        return self.id_number

    def get_hourly_rate(self):
        return self.hourly_rate


class PartTimeEmployee(Employee2):
    def __init__(self, name, id_number, hourly_rate, hours_worked):
        super().__init__(name, id_number, hourly_rate)
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked


class FullTimeEmployee(Employee2):
    def __init__(self, name, id_number, hourly_rate, monthly_salary):
        super().__init__(name, id_number, hourly_rate)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary


# Create a part-time employee object
part_time_employee = PartTimeEmployee("John Doe", 12345, 15.00, 20)

# Print the part-time employee's name and pay
print("Part-time employee name:", part_time_employee.get_name())
print("Part-time employee pay:", part_time_employee.calculate_pay())

# Create a full-time employee object
full_time_employee = FullTimeEmployee("Jane Smith", 56789, 20.00, 3000.00)

# Print the full-time employee's name and pay
print("Full-time employee name:", full_time_employee.get_name())
print("Full-time employee pay:", full_time_employee.calculate_pay())

def add(x, y):
    if type(x) == int and type(y) == int:
        return x + y
    elif type(x) == float and type(y) == float:
        return x + y
    elif type(x) == str and type(y) == str:
        return x + y
    else:
        print("Invalid data type")

print(add(10, 20))  # Output: 30
print(add(10.5, 20.5))  # Output: 31.0
print(add("Hello", "World"))  # Output: HelloWorld
print(add(10, "Hello"))  # Output: Invalid data type

class Pet:
    def make_sound(self):
        pass

class Dog(Pet):
    def make_sound(self):
        print("Woof!")

class Cat(Pet):
    def make_sound(self):
        print("Meow!")

def play_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

play_sound(dog)  # Output: Woof!
play_sound(cat)  # Output: Meow!


