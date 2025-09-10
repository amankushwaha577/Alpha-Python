# 🐍 Python OOP (Object-Oriented Programming)
# ───────────────────────────────────────────────

# 🔹 1. Classes and Objects
# ✅ Class = Blueprint (defines attributes + methods).
# ✅ Object = Instance of class.

class Car:
    def __init__(self, brand, model):  # constructor
        self.brand = brand
        self.model = model

    def drive(self):
        return f"{self.brand} {self.model} is driving!"


# Create objects (instances)
car1 = Car("Tesla", "Model S")
car2 = Car("BMW", "X5")

print(car1.drive())  # OUTPUT → Tesla Model S is driving!
print(car2.drive())  # OUTPUT → BMW X5 is driving!


# 🔹 2. Inheritance
# ✅ Mechanism to use parent class properties in child class.

class Animal:  # parent class
    def speak(self):
        return "I make sounds"


class Dog(Animal):  # child class inherits Animal
    def speak(self):
        return "Woof!"  # method overriding


d = Dog()
print(d.speak())  # OUTPUT → Woof!


# 🔹 3. @classmethod, @staticmethod, @property

class Student:
    school = "ABC School"  # class variable

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # classmethod → works with class (cls), not object
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # staticmethod → does not use self/cls (utility function)
    @staticmethod
    def is_passing(marks):
        return marks >= 40

    # property → getter (access attribute like variable)
    @property
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"


# Using the class
s1 = Student("Aman", 92)
print(s1.grade)  # OUTPUT → A (property, no need to call like function)

print(Student.school)  # OUTPUT → ABC School
Student.change_school("XYZ School")
print(Student.school)  # OUTPUT → XYZ School

print(Student.is_passing(50))  # OUTPUT → True
print(Student.is_passing(25))  # OUTPUT → False


# @classmethod → access class variables (cls).
# @staticmethod → utility, no self/cls.
# @property → turn method into attribute (getter/setter).