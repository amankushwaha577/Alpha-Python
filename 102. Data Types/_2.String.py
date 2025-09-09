# 🐍 Python Strings
# ───────────────────────────────────────────────
# ✅ Strings are sequences of characters enclosed in
#    single quotes (' '), double quotes (" "),
#    or triple quotes (''' ''' or """ """).
#
# Example:
s1 = 'Hello'
s2 = "World"
s3 = '''Multi
line
string'''
print(s1, s2, s3)

# ⚡ Key Points:
# 1. Strings in Python are immutable (you can’t change a character directly).
# 2. You can create substrings using slicing.
# 3. Use f-strings for formatting (fast & readable).


# 🔹 Common String Operations
# ───────────────────────────────────────────────
# Operation             | Example Code                | Result
# ───────────────────────────────────────────────
# Concatenation (+)     | "Hello" + "World"           | "HelloWorld"
# Repetition (*)        | "Hi" * 3                   | "HiHiHi"
# Indexing              | "Python"[0]                 | 'P'
# Negative Indexing     | "Python"[-1]                | 'n'
# Slicing               | "Python"[1:4]               | "yth"
# Length (len)          | len("Python")               | 6
# Membership (in)       | "Py" in "Python"            | True
# ───────────────────────────────────────────────


# 🔹 Useful String Methods
# ───────────────────────────────────────────────
# Method                | Example Code                | Result
# ───────────────────────────────────────────────
# upper()               | "hello".upper()             | "HELLO"
# lower()               | "Hello".lower()             | "hello"
# title()               | "hello world".title()       | "Hello World"
# strip()               | "  hi  ".strip()            | "hi"
# replace()             | "hi world".replace("hi","hello") | "hello world"
# split()               | "a,b,c".split(",")          | ['a','b','c']
# join()                | "-".join(['a','b','c'])     | "a-b-c"
# find()                | "python".find("th")         | 2
# count()               | "banana".count("a")         | 3
# startswith()          | "python".startswith("py")   | True
# endswith()            | "python".endswith("on")     | True
# format() (f-string)   | f"My age is {25}"           | "My age is 25"
# ───────────────────────────────────────────────


# ✅ Examples in Action:
s = "Python"
print(s[0])          # 'P'
print(s[-1])         # 'n'
print(s[2:5])        # "tho"
print("Py" in s)     # True
print(s.upper())     # "PYTHON"
print("a-b-c".split("-"))  # ['a','b','c']
print("-".join(["2025","09","10"]))  # "2025-09-10"


# 🐍 Why are Strings Immutable in Python?
# ───────────────────────────────────────────────
# ✅ Immutable means: Once created, you cannot change it directly.
#    If you "modify" a string, Python actually creates a new object.
#
# Example:
s = "Hello"
print(id(s))   # Suppose memory address = 1401
s = s + " World"
print(id(s))   # New memory address = 1520 (different!)

# ⚡ Memory Diagram
# ───────────────────────────────────────────────
# Step 1: Create string "Hello"
#   ┌───────────┐       ┌─────────────┐
#   │ Variable s │ ────▶ │ "Hello"     │ (Addr: 1401)
#   └───────────┘       └─────────────┘
#
# Step 2: Append " World"
#   - Old "Hello" stays in memory (garbage collected later if unused).
#   - New string "Hello World" created at a new location.
#
#   ┌───────────┐       ┌─────────────┐
#   │ Variable s │ ────▶ │ "Hello World" │ (Addr: 1520)
#   └───────────┘       └─────────────┘
#
# ❌ You never modified "Hello". Instead, you created a new string!
#
# ✅ Advantages of Immutability:
# 1. Thread-safety (no accidental changes).
# 2. String interning → saves memory (reusing same literal).
# 3. Security (useful in keys, constants).
