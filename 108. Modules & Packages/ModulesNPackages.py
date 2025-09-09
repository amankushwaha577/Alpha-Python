# 🐍 Python Modules & Packages
# ───────────────────────────────────────────────
# ✅ Module = A file containing Python code (functions, classes, variables).
# ✅ Package = A collection of modules in a directory with __init__.py.
# ✅ We use "import" to bring in modules/packages.


# 🔹 1. Importing Libraries (Built-in Module)
import math

print(math.sqrt(16))       # OUTPUT → 4.0
print(math.pi)             # OUTPUT → 3.141592653589793

from math import factorial
print(factorial(5))        # OUTPUT → 120


# 🔹 2. Creating Your Own Module
# Step 1 → Create a file called mymodule.py with this content:
# ---------------------------------
# def greet(name):
#     return f"Hello, {name}!"
#
# def add(a, b):
#     return a + b
# ---------------------------------

# Step 2 → Import and use it in another file (main.py)
import mymodule

print(mymodule.greet("Aman"))   # OUTPUT → Hello, Aman!
print(mymodule.add(3, 4))       # OUTPUT → 7


# 🔹 3. Using pip to Install External Packages
# pip = Python’s package manager (comes with Python).
# Example (installing requests library):
# ---------------------------------
# pip install requests
# ---------------------------------

# After installation, we can use it:
import requests

response = requests.get("https://api.github.com")
print(response.status_code)    # OUTPUT → 200 (OK if request successful)
print(response.json()["current_user_url"])  # sample JSON key


# ⚡ Summary
# ───────────────────────────────────────────────
# Feature                 | Example
# ───────────────────────────────────────────────
# Import Built-in Module  | import math
# From Import             | from math import sqrt
# Custom Module           | import mymodule
# Package Installation    | pip install requests
# ───────────────────────────────────────────────
