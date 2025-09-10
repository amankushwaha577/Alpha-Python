# 🐍 1. Decorators
# ───────────────────────────────────────────────
# ✅ A decorator is a function that takes another function
#    as input and adds extra functionality to it,
#    without changing its original code.
#
# ✅ Syntax: @decorator_name


def my_decorator(func):
    # func → the original function (here greet)
    def wrapper():
        print("Before function call")   # extra behavior
        func()                          # call original function
        print("After function call")    # extra behavior
    return wrapper   # return new wrapped function


# ✅ Using @my_decorator is same as:
# greet = my_decorator(greet)

@my_decorator
def greet():
    print("Hello!")


# 🔹 How it works step by step:
# 1. Python sees @my_decorator above greet().
# 2. It replaces greet with: greet = my_decorator(greet)
# 3. my_decorator receives the original greet as func.
# 4. my_decorator returns wrapper, so greet now points to wrapper.
# 5. When we call greet(), wrapper() runs:
#       → prints "Before function call"
#       → calls the original greet() → prints "Hello!"
#       → prints "After function call"

greet()

# 🔹 Output:
# Before function call
# Hello!
# After function call
