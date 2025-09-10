# 🐍 Generators in Python
# ───────────────────────────────────────────────
# ✅ A Generator is a special type of function that returns
#    an iterator object using 'yield' instead of 'return'.
# ✅ They produce values one at a time → "lazy evaluation".
# ✅ They save memory compared to lists.


# 🔹 1. Normal Function vs Generator
def normal_list(n):
    return [i for i in range(n)]

def generator_func(n):
    for i in range(n):
        yield i

print(normal_list(5))           # OUTPUT → [0, 1, 2, 3, 4]
print(list(generator_func(5)))  # OUTPUT → [0, 1, 2, 3, 4]

# Difference:
# - normal_list → creates the entire list in memory at once.
# - generator_func → produces one value at a time (on demand).


# 🔹 2. Using next() with Generator
gen = generator_func(3)
print(next(gen))   # OUTPUT → 0
print(next(gen))   # OUTPUT → 1
print(next(gen))   # OUTPUT → 2
# next(gen) would raise StopIteration


# 🔹 3. Generator Expression (like list comprehension but with ())
gen_exp = (x*x for x in range(5))
print(gen_exp)             # OUTPUT → <generator object ...>
print(list(gen_exp))       # OUTPUT → [0, 1, 4, 9, 16]


# 🔹 4. Infinite Generators (good for streams)
def infinite_numbers():
    n = 0
    while True:
        yield n
        n += 1

gen_inf = infinite_numbers()
print(next(gen_inf))   # OUTPUT → 0
print(next(gen_inf))   # OUTPUT → 1
print(next(gen_inf))   # OUTPUT → 2
# ... goes forever


# 🔹 5. Memory Comparison (list vs generator)
import sys

list_nums = [i for i in range(1000000)]
gen_nums = (i for i in range(1000000))

print(sys.getsizeof(list_nums))  # OUTPUT → large (takes MBs)
print(sys.getsizeof(gen_nums))   # OUTPUT → very small (just bytes)


# ⚡ Summary
# ───────────────────────────────────────────────
# Feature           | Generator
# ───────────────────────────────────────────────
# Syntax            | Uses yield
# Execution         | Lazy (one value at a time)
# Memory Usage      | Very low (doesn’t store all values)
# Convert to list   | list(generator)
# Infinite Stream   | ✅ possible
# Common Use Cases  | Big data, streaming, pipelines
# ───────────────────────────────────────────────
