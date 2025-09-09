# 🐍 Python Boolean Type → bool
# ───────────────────────────────────────────────
# ✅ Boolean represents only two values: True or False.
# ✅ Used in conditions, comparisons, and logical operations.

# 🔹 Creating Booleans
flag = True
is_active = False
print(flag)         # OUTPUT → True
print(is_active)    # OUTPUT → False


# 🔹 From Comparisons (result is always bool)
print(10 > 5)       # OUTPUT → True
print(3 == 4)       # OUTPUT → False
print("a" in "apple")   # OUTPUT → True


# 🔹 Logical Operators
a, b = True, False
print(a and b)      # OUTPUT → False  (both must be True)
print(a or b)       # OUTPUT → True   (at least one True)
print(not a)        # OUTPUT → False  (negation)


# 🔹 Boolean as Numbers
# ✅ Internally, bool is a subclass of int:
# True → 1 , False → 0
print(True + True)   # OUTPUT → 2
print(True * 5)      # OUTPUT → 5
print(False + 10)    # OUTPUT → 10


# ⚡ Summary
# ───────────────────────────────────────────────
# Type     | Values       | Example
# ───────────────────────────────────────────────
# bool     | True / False | flag = True
# ───────────────────────────────────────────────
