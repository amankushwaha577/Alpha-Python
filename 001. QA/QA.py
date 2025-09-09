# 🐍 Loops & Conditions — Interview Q&A
# ───────────────────────────────────────────────

# 🔹 1. Difference between for loop and while loop?
# - for loop → Used when you know the number of iterations (iterates over iterable).
# - while loop → Used when you don’t know in advance; runs until condition is False.


# 🔹 2. Role of 'elif' in Python?
# - It allows multiple conditions without writing nested if.
x = 15
if x > 20:
    print("Greater than 20")
elif x == 15:
    print("Exactly 15")
else:
    print("Less than 20")
# OUTPUT → Exactly 15


# 🔹 3. Can we write if without else?
# ✅ Yes, else is optional.
if 5 > 2:
    print("Yes")
# OUTPUT → Yes


# 🔹 4. What does 'pass' do?
# - It is a placeholder → does nothing.
for i in range(3):
    pass
print("Loop executed")
# OUTPUT → Loop executed


# 🔹 5. How is Python's 'for' loop different from Java/C++?
# - In Java/C++: for uses index (i=0; i<n; i++).
# - In Python: for directly iterates over iterable.
for ch in "ABC":
    print(ch)
# OUTPUT → A B C


# 🔹 6. Predict output:
x = 0
while x < 3:
    print(x)
    x += 1
# OUTPUT →
# 0
# 1
# 2


# 🔹 7. Predict output:
for i in range(5):
    if i == 2:
        break
    print(i)
# OUTPUT →
# 0
# 1


# 🔹 8. Largest of 3 numbers
a, b, c = 10, 25, 15
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
# OUTPUT → Largest: 25


# 🔹 9. Prime Number Check
n = 11
is_prime = True
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
print("Prime" if is_prime else "Not Prime")
# OUTPUT → Prime


# 🔹 10. Fibonacci sequence (first 6 terms)
n = 6
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
# OUTPUT → 0 1 1 2 3 5


# 🔹 11. Palindrome Check
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
# OUTPUT → Palindrome


# 🔹 12. Multiplication Table (of 5)
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
# OUTPUT →
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50


# 🔹 13. What happens with while True: without break?
# - Infinite loop (program runs forever unless stopped).
# Example:
# while True:
#     print("infinite")   # ❌ WARNING: don't run, will never stop


# 🔹 14. Iterating over dictionary
person = {"name": "Aman", "age": 25}
for key, value in person.items():
    print(key, ":", value)
# OUTPUT →
# name : Aman
# age : 25


# 🔹 15. Difference between break and continue
for i in range(5):
    if i == 2:
        break   # exit loop
    print("break loop →", i)
# OUTPUT → 0, 1

for i in range(5):
    if i == 2:
        continue   # skip 2
    print("continue loop →", i)
# OUTPUT → 0, 1, 3, 4


# 🔹 16. Can we use else with loop?
for i in range(3):
    print(i)
else:
    print("Loop finished")
# OUTPUT →
# 0
# 1
# 2
# Loop finished
