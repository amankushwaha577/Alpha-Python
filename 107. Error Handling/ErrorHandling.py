# 🐍 Python Error Handling
# ───────────────────────────────────────────────
# ✅ Errors in Python are called "Exceptions".
# ✅ We use try-except-finally to handle exceptions gracefully.
# ✅ We can also raise custom exceptions using raise.


# 🔹 1. try–except
try:
    x = 10 / 0     # division by zero error
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# OUTPUT → Error: Cannot divide by zero!


# 🔹 2. Multiple except blocks
try:
    num = int("abc")   # ValueError
except ValueError:
    print("Invalid conversion to integer")
except ZeroDivisionError:
    print("Cannot divide by zero")

# OUTPUT → Invalid conversion to integer


# 🔹 3. try–except–finally
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file/resources (always runs)")

# OUTPUT →
# File not found
# Closing file/resources (always runs)


# 🔹 4. Raise custom error
age = 15
if age < 18:
    raise ValueError("Age must be 18 or above to register")

# OUTPUT →
# Traceback (most recent call last):
#   ...
# ValueError: Age must be 18 or above to register


# ⚡ Summary
# ───────────────────────────────────────────────
# Block      | Usage
# ───────────────────────────────────────────────
# try        | Put code that may raise error
# except     | Handle the error gracefully
# finally    | Always executes (cleanup, closing files/db)
# raise      | Throw custom errors manually
# ───────────────────────────────────────────────
