# 1. Comprehensions :
# -------------------
# Shortcut for creating lists/sets/dicts.

squares = [x*x for x in range(5)]  # [0,1,4,9,16]
evens = [x for x in range(10) if x % 2 == 0]

# 2. Swapping: a, b = b, a

# 3. Unpacking: x, y, *rest = [1,2,3,4]

# 4. Ternary: res = "Yes" if x>0 else "No"
