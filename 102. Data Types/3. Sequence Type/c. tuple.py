# 🐍 Python Tuple Functions / Methods
# ───────────────────────────────────────────────
# ✅ Tuples are ordered, immutable collections.
# ✅ Once created, elements cannot be added, removed, or modified.
# ✅ Only a few methods are available.


# ⚡ Summary Table
# ───────────────────────────────────────────────
# Modifies Tuple (in-place)   | ❌ None (Tuples are immutable)
# ────────────────────────────|───────────────────────────────
# Does NOT Modify (returns)   | count(), index(),
#                             | len(), min(), max(), sum(),
#                             | sorted()
# ───────────────────────────────────────────────

# ⚡ Quick Rule:
# - Tuples do not support modification methods (append, remove, clear, etc.).
# - Only query methods and built-in functions work.


# ───────────────────────────────────────────────
# 🔹 METHODS / FUNCTIONS THAT DO NOT MODIFY
# ───────────────────────────────────────────────
t = (1, 2, 2, 3, 4)

# count(value) → count occurrences
print(t.count(2))     # OUTPUT → 2

# index(value) → find first position
print(t.index(3))     # OUTPUT → 3

# len() → number of elements
print(len(t))         # OUTPUT → 5

# min() / max()
print(min(t))         # OUTPUT → 1
print(max(t))         # OUTPUT → 4

# sum() → total of elements
print(sum(t))         # OUTPUT → 12

# sorted() → returns NEW sorted list (not tuple)
print(sorted(t))      # OUTPUT → [1, 2, 2, 3, 4]
print(t)              # OUTPUT → (1, 2, 2, 3, 4) (unchanged)


# ⚡ Note:
# Tuples are immutable → to "modify", you must convert to a list:
temp = list(t)
temp.append(5)
t = tuple(temp)
print(t)              # OUTPUT → (1, 2, 2, 3, 4, 5)
