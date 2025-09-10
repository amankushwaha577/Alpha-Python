
# 🐍 Difference between "is" and "=="
# ───────────────────────────────────────────────
# ✅ "==" → Checks VALUE equality
# ✅ "is" → Checks IDENTITY ((memory address)) (whether two variables point to the same object in memory)


# 🔹 Example 1: Same values, different objects
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  → because values are same
print(a is b)   # False → because stored at different memory addresses


# 🔹 Example 2: Assignment (same object)
x = [10, 20]
y = x
print(x == y)   # True → values same
print(x is y)   # True → both refer to same object


# 🔹 Example 3: Immutable small integers (Python caches them)
p = 5
q = 5
print(p == q)   # True
print(p is q)   # True → same memory (due to caching)


# 🔹 Example 4: Strings (sometimes cached, sometimes not)
s1 = "hello"
s2 = "hello"
print(s1 == s2)  # True
print(s1 is s2)  # True (cached in memory)

s3 = "".join(["he", "llo"])
print(s1 == s3)  # True → values same
print(s1 is s3)  # False → different object in memory
