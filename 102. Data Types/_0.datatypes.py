# 🐍 Python Data Types
# ──────────────────────────────────────────────────────────────
# Category          | Data Type        | Example
# ──────────────────────────────────────────────────────────────
# Numeric Types     | int              | x = 10
#                   | float            | y = 3.14
#                   | complex          | z = 2 + 3j
# ──────────────────────────────────────────────────────────────
# Text Type         | str (string)     | name = "Aman"
# ──────────────────────────────────────────────────────────────
# Sequence Types    | list             | nums = [1, 2, 3]
#                   | tuple            | point = (3, 4)
#                   | range            | r = range(5)  # 0 to 4
# ──────────────────────────────────────────────────────────────
# Set Types         | set              | s = {1, 2, 3}
#                   | frozenset        | fs = frozenset([1, 2, 3])
# ──────────────────────────────────────────────────────────────
# Mapping Type      | dict             | student = {"name": "Aman", "age": 25}
# ──────────────────────────────────────────────────────────────
# Boolean Type      | bool             | flag = True
# ──────────────────────────────────────────────────────────────
# Binary Types      | bytes            | b = b"hello"
#                   | bytearray        | ba = bytearray(5)
#                   | memoryview       | mv = memoryview(b"hello")
# ──────────────────────────────────────────────────────────────

# Q. Mutable vs Immutable types?
# → Mutable: list, dict, set.
#   Immutable: int, float, str, tuple.
#
# Q. Difference between list, tuple, set, dict?
#  → list = ordered, mutable.
#    tuple = ordered, immutable.
#    set = unordered unique values.
#    dict = key–value pairs.


# ✅ Examples in Action:
x = 10                 # int
y = 3.14               # float
z = 2 + 3j             # complex

name = "Aman"          # string

nums = [1, 2, 3]       # list
point = (3, 4)         # tuple

s = {1, 2, 3}          # set

student = {"name": "Aman", "age": 25}  # dict
flag = True            # bool


print(x)
