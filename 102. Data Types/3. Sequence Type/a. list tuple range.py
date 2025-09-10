# 🐍 Python Sequence Types
# ───────────────────────────────────────────────
# 1️⃣ list  → Ordered, mutable (can change elements)
# 2️⃣ tuple → Ordered, immutable (cannot change once created)
# 3️⃣ range → Generates a sequence of numbers (commonly used in loops)

# 🔹 List (Mutable)
nums = [1, 2, 3]
nums[0] = 10          # ✅ allowed (mutability)
nums.append(4)        # ✅ add new element
print(nums)           # [10, 2, 3, 4]

# 🔹 Tuple (Immutable)
point = (3, 4)
# point[0] = 5   ❌ ERROR (tuples cannot be modified)
print(point)          # (3, 4)

# 🔹 Range (Sequence Generator)
r = range(5)          # numbers from 0 to 4
print(list(r))        # [0, 1, 2, 3, 4]


# ⚡ Summary
# ───────────────────────────────────────────────
# Type     | Mutable? | Ordered? | Example
# ───────────────────────────────────────────────
# list     | Yes      | Yes      | [1, 2, 3]
# tuple    | No       | Yes      | (3, 4)
# range    | No       | Yes      | range(0,5) → 0..4
# ───────────────────────────────────────────────
