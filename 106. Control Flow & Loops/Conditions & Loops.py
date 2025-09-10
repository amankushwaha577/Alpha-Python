# 🐍 Python Conditions & Loops
# ───────────────────────────────────────────────
# ✅ Used for decision making & repetition in programs.


# 🔹 1. Conditions (if / elif / else)
x = 15
if x > 20:
    print("x is greater than 20")
elif x == 15:
    print("x is exactly 15")
else:
    print("x is smaller than 20")

# OUTPUT → x is exactly 15


# 🔹 2. For Loop (iterate over sequence)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# OUTPUT →
# apple
# banana
# cherry


# 🔹 3. For Loop with range()
for i in range(1, 6):
    print(i)

# OUTPUT →
# 1
# 2
# 3
# 4
# 5


# 🔹 4. While Loop (repeat until condition false)
count = 1
while count <= 3:
    print("Count:", count)
    count += 1

# OUTPUT →
# Count: 1
# Count: 2
# Count: 3


# 🔹 5. Loop Control Statements
for i in range(5):
    if i == 2:
        continue   # skips 2
    if i == 4:
        break      # stops loop at 4
    print(i)

# OUTPUT →
# 0
# 1
# 3


# 🔹 6. pass Statement (do nothing placeholder)
for i in range(3):
    pass
print("Loop executed with pass (no action)")

# OUTPUT → Loop executed with pass (no action)


# ⚡ Summary
# ───────────────────────────────────────────────
# Conditionals → if, elif, else
# Loops → for (sequence iteration), while (repeat until condition)
# Controls → break (exit), continue (skip), pass (do nothing)
# ───────────────────────────────────────────────


# Que. Difference between break, continue, pass?
# Ans. → break = exit loop, continue = skip iteration, pass = do nothing.
#
# Que. Can loops have an else?
# Ans. → Yes! Runs if loop finishes normally (not broken).