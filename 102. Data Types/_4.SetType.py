# 🐍 Python Sets
# ───────────────────────────────────────────────
# ✅ A set is:
# - An unordered collection of unique elements (no duplicates).
# - Mutable (we can add/remove elements).
# - Does not allow indexing (like s[0] ❌).
# - Very fast for membership tests (because internally uses hash table).

# 🔹 Creating a Set
s = {1, 2, 3, 3, 4}
print(s)       # {1, 2, 3, 4}  (duplicates removed)

empty_set = set()   # correct way to create empty set
# empty = {}        # ❌ This makes a dictionary, not a set

# Diagram:
# ┌───────────┐
# │ s         │──▶ {1, 2, 3, 4}
# └───────────┘


# 🔹 Adding & Removing
s.add(5)       # {1, 2, 3, 4, 5}
s.remove(2)    # {1, 3, 4, 5}
s.discard(10)  # No error if element not found
print(s)


# 🔹 Set Operations (like in Math)
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)    # Union → {1, 2, 3, 4, 5}
print(a & b)    # Intersection → {3}
print(a - b)    # Difference → {1, 2}
print(a ^ b)    # Symmetric Difference → {1, 2, 4, 5}

# 🔹 Membership Test
print(3 in a)   # True
print(6 in a)   # False


# ⚡ Summary
# ───────────────────────────────────────────────
# Feature              | Set
# ───────────────────────────────────────────────
# Unique Elements      | ✅ (no duplicates allowed)
# Ordered?             | ❌ (no guaranteed order)
# Indexing             | ❌ Not allowed
# Mutable              | ✅ Yes (can add/remove)
# Common Use           | Fast membership test, removing duplicates
# ───────────────────────────────────────────────
