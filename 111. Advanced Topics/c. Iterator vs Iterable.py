# 🐍 3. Iterator vs Iterable
# ───────────────────────────────────────────────
# ✅ Iterable: An object you can loop over (list, tuple, string, etc.).
# ✅ Iterator: An object that remembers its position and gives values
#    one at a time using __next__().

nums = [10, 20, 30]       # list is iterable
it = iter(nums)           # convert iterable to iterator

print(next(it))   # OUTPUT → 10
print(next(it))   # OUTPUT → 20
print(next(it))   # OUTPUT → 30
# print(next(it)) # ❌ StopIteration error if no more items

# RULE:
# - Iterable → has __iter__()
# - Iterator → has both __iter__() and __next__()
