# 🐍 Python Numeric Types
# ───────────────────────────────────────────────
# 1. int     → Integer numbers (whole numbers)
#              Example: 10, -5, 0
#
# 2. float   → Decimal numbers (real numbers)
#              Example: 3.14, -2.7, 0.0
#
# 3. complex → Numbers with real + imaginary part
#              Example: 2 + 3j, 5 - 6j
#
# ✅ Python automatically chooses type based on value.
# ✅ You can check type using: type(x)


# 🧮 Common Numeric Operations
# ───────────────────────────────────────────────
# Operator   | Meaning                     | Example
# ───────────────────────────────────────────────
# +          | Addition                    | 5 + 3 = 8
# -          | Subtraction                 | 5 - 3 = 2
# *          | Multiplication              | 5 * 3 = 15
# /          | Division (float result)     | 5 / 2 = 2.5
# //         | Floor division (quotient)   | 5 // 2 = 2
# %          | Modulus (remainder)         | 5 % 2 = 1
# **         | Exponent (power)            | 2 ** 3 = 8
# abs()      | Absolute value              | abs(-7) = 7
# pow(a, b)  | a raised to power b         | pow(2, 4) = 16
# round(x,n) | Round to n decimals         | round(3.14159, 2) = 3.14


# ✅ Examples in Action:
a = 10        # int
b = 3.5       # float
c = 2 + 3j    # complex

print(a + b)        # 13.5
print(a // 3)       # 3
print(a % 3)        # 1
print(a ** 2)       # 100
print(abs(-25))     # 25
print(pow(2, 5))    # 32
print(round(3.14159, 3))  # 3.142
print(c * (1 + 2j)) # Complex multiplication → (2+3j)*(1+2j) = -4+7j



# 🐍 Python vs ☕ Java → Numeric Operations
# ──────────────────────────────────────────────────────────────
# Operation        | Python Example           | Java Example
# ──────────────────────────────────────────────────────────────
# Division (/)     | 5 / 2 = 2.5  (always float)| 5 / 2 = 2 (integer if both are int)
#                  | 5 / 2.0 = 2.5              | 5 / 2.0 = 2.5 (float/double division)
# ──────────────────────────────────────────────────────────────
# Floor Division   | 5 // 2 = 2                | No direct operator, use (5 / 2)
# (integer result) | (works with negatives too)| but careful with negatives
# ──────────────────────────────────────────────────────────────
# Modulus (%)      | 5 % 2 = 1                 | 5 % 2 = 1
#                  | (-5) % 2 = 1 ✅            | (-5) % 2 = -1 ⚠️ different!
# ──────────────────────────────────────────────────────────────
# Exponentiation   | 2 ** 3 = 8                | No operator, use Math.pow(2,3)
# ──────────────────────────────────────────────────────────────
# Complex Numbers  | 2 + 3j (built-in support) | ❌ Not supported directly,
#                  |                          | need external libraries
# ──────────────────────────────────────────────────────────────
# Big Numbers      | Python int is unlimited   | Java int has 32-bit limit,
#                  | (arbitrary precision)     | use BigInteger for very large values
# ──────────────────────────────────────────────────────────────

# ✅ Key Takeaways:
# A. 5 % 2 = 1 is same in both Python and Java when numbers are positive.

# B. Negative modulus differs:
#    🐍 Python Behavior : modulus (%) result always has the **same sign as the divisor.
#    Python: (-5) % 2 = 1 (always result has the same sign as divisor).
#    print(5 % -2)   # Output: -1

#    ☕ Java Behavior : Rule: In Java, modulus (%) result always has the **same sign as the dividend
#    Java: (-5) % 2 = -1 (result has the same sign as dividend).
#    System.out.println(5 % -2);   // Output: 1

# C. Division / in Python always gives float, but in Java it depends on operand types.
#
# D. Python has built-in support for big integers & complex numbers, Java doesn’t.
