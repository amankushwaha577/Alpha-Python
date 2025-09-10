# 🐍 Python Functions
# ───────────────────────────────────────────────
# ✅ A function is a block of reusable code that performs a specific task.
# ✅ Functions help in modularity, reusability, and clean code.


# 🔹 1. Defining and Calling Functions
def greet():
    print("Hello, welcome to Python!")

greet()
# OUTPUT → Hello, welcome to Python!


# 🔹 2. Parameters & Return Values
def add(a, b):
    return a + b

result = add(5, 7)
print(result)
# OUTPUT → 12


# 🔹 3. Default Arguments
def welcome(name="Guest"):
    print("Hello", name)

welcome("Aman")    # OUTPUT → Hello Aman
welcome()          # OUTPUT → Hello Guest  (uses default)


# 🔹 4. Keyword Arguments
def intro(name, age):
    print(f"My name is {name}, and I am {age} years old.")

intro(age=25, name="Aman")  #this way is called as keyword arguments.
# OUTPUT → My name is Aman, and I am 25 years old.


# 🔹 5. Lambda Functions (Anonymous Functions)
# ✅ Short one-line functions without 'def'
square = lambda x: x * x
print(square(5))
# OUTPUT → 25

add_nums = lambda a, b: a + b
print(add_nums(3, 4))
# OUTPUT → 7


# ⚡ Summary
# ───────────────────────────────────────────────
# Feature                 | Example
# ───────────────────────────────────────────────
# Define + Call           | def f(): ... ; f()
# Parameters + Return     | def f(a,b): return a+b
# Default Arguments       | def f(x=10): ...
# Keyword Arguments       | f(age=25, name="Aman")
# Lambda Functions        | f = lambda x: x*x
# ───────────────────────────────────────────────
