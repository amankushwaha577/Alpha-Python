# 🐍 Python Type Conversion (Casting)
# ───────────────────────────────────────────────
# ✅ Type conversion means converting one data type into another.
# ✅ Two types:
# 1. Implicit conversion (done by Python automatically).
# 2. Explicit conversion (done manually using int(), float(), str()).


# 🔹 Implicit Conversion (automatic)
x = 5          # int
y = 2.5        # float
z = x + y      # int + float → float
print(z)       # OUTPUT → 7.5
print(type(z)) # OUTPUT → <class 'float'>


# 🔹 Explicit Conversion (manual casting)
# int() → convert to integer (decimal part removed)
a = int(3.9)
print(a)       # OUTPUT → 3

# float() → convert to float
b = float(10)
print(b)       # OUTPUT → 10.0

# str() → convert to string
c = str(100)
print(c)       # OUTPUT → "100"
print(type(c)) # OUTPUT → <class 'str'>


# 🔹 String to Number Conversion
num_str = "25"
print(int(num_str) + 5)    # OUTPUT → 30

# ❌ If string is not numeric, error occurs:
# int("hello") → ValueError


# 🔹 Number to String Conversion
age = 25
msg = "I am " + str(age) + " years old."
print(msg)
# OUTPUT → "I am 25 years old."


# ⚡ Summary
# ───────────────────────────────────────────────
# Function   | Converts To      | Example
# ───────────────────────────────────────────────
# int(x)     | Integer          | int(3.7) → 3
# float(x)   | Float            | float(5) → 5.0
# str(x)     | String           | str(10) → "10"
# ───────────────────────────────────────────────
