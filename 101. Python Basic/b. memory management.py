# 🐍 Python Memory Management
# ───────────────────────────────────────────────

# ✅ How Python Manages Memory
# - Python uses a **private heap space** to store all objects and data structures.
# - Memory management is handled by:
#   (a) Reference Counting
#   (b) Garbage Collector (to handle cycles)
#   (c) Memory Pools (handled internally by PyMalloc)

# ✅ 1. Reference Counting
# - Every object has a counter → how many variables refer to it.
# - When count → 0 → object is deleted from memory.

a = [1, 2, 3]
b = a                # both point to same list
print(id(a), id(b))  # same memory address
# OUTPUT → (e.g. 140712345678, 140712345678)
# Ref count for [1,2,3] = 2 (a and b)

del a
# Now ref count = 1 (only b refers)

del b
# Now ref count = 0 → object destroyed by GC


# ✅ 2. Garbage Collection
# - Python automatically deletes objects with ref count 0.
# - Uses cyclic GC to clean circular references.

import gc
print(gc.isenabled())   # OUTPUT → True
# gc.collect() → forces garbage collection manually


# ✅ 3. Memory Pools (PyMalloc)
# - For efficiency, Python maintains memory pools of fixed sizes.
# - This avoids calling system malloc/free frequently.




#  Example: Object Reuse (small integers, strings are cached)
x = 10
y = 10
print(id(x), id(y))   # Same ID (Python reuses small ints)

s1 = "hello"
s2 = "hello"
print(id(s1), id(s2)) # Same ID (string interning)


# ⚡ Diagram (Reference Counting Example)
# ───────────────────────────────────────────────
# a = [1,2,3]   → ref count = 1
# b = a         → ref count = 2
# del a         → ref count = 1
# del b         → ref count = 0 → GC cleans object
