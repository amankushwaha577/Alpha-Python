# 🐍 Python List Functions / Methods
# ───────────────────────────────────────────────
# ✅ Lists are ordered, mutable collections.
# ✅ Below methods actually MODIFY the list in-place.

# ⚡ Summary Table
# ───────────────────────────────────────────────
# Modifies List (in-place)   | append(), insert(), extend(),
#                            | remove(), pop(), sort(),
#                            | reverse(), clear()
# ───────────────────────────|───────────────────────────────
# Does NOT Modify (returns)  | index(), count(), copy(),
#                            | len(), min(), max(), sum(),
#                            | sorted()

# ⚡ Quick Rule:
# 1. If it returns None → it modified the list in-place.
# 2. If it returns a value/list → it does NOT modify the original.


# ───────────────────────────────────────────────
# 🔹 METHODS THAT MODIFY THE LIST (in-place)
# ───────────────────────────────────────────────

# 🔹 1. append() → Add element at end  ✅ modifies
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)
# OUTPUT → ['apple', 'banana', 'cherry']


# 🔹 2. insert(index, value) → Insert at position  ✅ modifies
fruits.insert(1, "orange")
print(fruits)
# OUTPUT → ['apple', 'orange', 'banana', 'cherry']


# 🔹 3. extend(list) → Add multiple elements  ✅ modifies
fruits.extend(["mango", "grape"])
print(fruits)
# OUTPUT → ['apple', 'orange', 'banana', 'cherry', 'mango', 'grape']


# 🔹 4. remove(value) → Remove first occurrence  ✅ modifies
fruits.remove("banana")
print(fruits)
# OUTPUT → ['apple', 'orange', 'cherry', 'mango', 'grape']


# 🔹 5. pop(index) → Remove and return element (default last)  ✅ modifies
last = fruits.pop()
print(last)      # OUTPUT → grape
print(fruits)    # OUTPUT → ['apple', 'orange', 'cherry', 'mango']


# 🔹 8. sort() → Sort list in ascending (in-place)  ✅ modifies
nums = [1, 2, 2, 3, 2, 4]
nums.sort()
print(nums)
# OUTPUT → [1, 2, 2, 2, 3, 4]

# Descending sort
nums.sort(reverse=True)
print(nums)
# OUTPUT → [4, 3, 2, 2, 2, 1]


# 🔹 9. reverse() → Reverse the list  ✅ modifies
nums.reverse()
print(nums)
# OUTPUT → [1, 2, 2, 2, 3, 4]


# 🔹 11. clear() → Empty the list  ✅ modifies
fruits.clear()
print(fruits)
# OUTPUT → []



# ───────────────────────────────────────────────
# 🔹 METHODS / FUNCTIONS THAT DO NOT MODIFY (return value)
# ───────────────────────────────────────────────
nums = [1, 2, 2, 3, 2, 4]

# index(value) → find first position
print(nums.index(3))     # 3

# count(value) → count occurrences
print(nums.count(2))     # 3

# copy() → shallow copy
copy_list = nums.copy()
print(copy_list)         # [1, 2, 2, 3, 2, 4]

# len() → number of elements
print(len(nums))         # 6

# min() / max()
print(min(nums))         # 1
print(max(nums))         # 4

# sum() → total of elements
print(sum(nums))         # 14

# sorted() → returns NEW sorted list (doesn’t modify original)
print(sorted(nums))      # [1, 2, 2, 2, 3, 4]
print(nums)              # [1, 2, 2, 3, 2, 4] (unchanged)