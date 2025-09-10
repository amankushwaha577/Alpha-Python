# ⚡ Summary Table
# ───────────────────────────────────────────────
# Modifies Set (in-place)   | add(), update(), remove(),
#                           | discard(), pop(), clear()
# ──────────────────────────|───────────────────────────────
# Does NOT Modify (returns) | union(), intersection(),
#                           | difference(), symmetric_difference(),
#                           | issubset(), issuperset(), isdisjoint(),
#                           | copy(), len(), min(), max(), sum(), sorted()
# ───────────────────────────────────────────────

# ⚡ Quick Rule:
# - Methods ending with "update" or direct mutations → modify set.
# - Operations that produce new sets → return values (do not modify).


# ───────────────────────────────────────────────
# 🔹 METHODS THAT MODIFY THE SET (in-place)
# ───────────────────────────────────────────────
s = {1, 2, 3}

# add(value) → add single element
s.add(4)
print(s)        # OUTPUT → {1, 2, 3, 4}

# update(iterable) → add multiple elements
s.update([5, 6])
print(s)        # OUTPUT → {1, 2, 3, 4, 5, 6}

# remove(value) → remove element (error if not found)
s.remove(3)
print(s)        # OUTPUT → {1, 2, 4, 5, 6}

# discard(value) → remove element (no error if not found)
s.discard(10)
print(s)        # OUTPUT → {1, 2, 4, 5, 6}

# pop() → remove and return arbitrary element
removed = s.pop()
print(removed)
print(s)        # OUTPUT → One element removed (random)

# clear() → empty set
s.clear()
print(s)        # OUTPUT → set()


# ───────────────────────────────────────────────
# 🔹 METHODS / FUNCTIONS THAT DO NOT MODIFY
# ───────────────────────────────────────────────
a = {1, 2, 3}
b = {3, 4, 5}

# union() → all unique elements
print(a.union(b))             # OUTPUT → {1, 2, 3, 4, 5}

# intersection() → common elements
print(a.intersection(b))      # OUTPUT → {3}

# difference() → elements in a not in b
print(a.difference(b))        # OUTPUT → {1, 2}

# symmetric_difference() → elements in either, not both
print(a.symmetric_difference(b))  # OUTPUT → {1, 2, 4, 5}

# issubset(), issuperset(), isdisjoint()
print({1, 2}.issubset(a))     # OUTPUT → True
print(a.issuperset({1}))      # OUTPUT → True
print(a.isdisjoint({7, 8}))   # OUTPUT → True

# copy()
c = a.copy()
print(c)                      # OUTPUT → {1, 2, 3}

# Built-in functions
nums = {10, 20, 30}
print(len(nums))              # OUTPUT → 3
print(min(nums))              # OUTPUT → 10
print(max(nums))              # OUTPUT → 30
print(sum(nums))              # OUTPUT → 60
print(sorted(nums))           # OUTPUT → [10, 20, 30] (list)
