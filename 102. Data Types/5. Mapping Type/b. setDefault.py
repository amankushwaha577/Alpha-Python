# 🐍 dict.setdefault(key, default)
# ───────────────────────────────────────────────
# ✅ Behavior:
# 1. If key exists → return its value (dict unchanged).
# 2. If key does NOT exist → insert it with given default value, then return that default.


# Example 1: Key does not exist
student = {"name": "Aman"}
print(student.setdefault("country", "India"))   # OUTPUT → India
print(student)
# OUTPUT → {'name': 'Aman', 'country': 'India'}
# (new key 'country' added)


# Example 2: Key already exists
student = {"name": "Aman", "country": "USA"}
print(student.setdefault("country", "India"))   # OUTPUT → USA
print(student)
# OUTPUT → {'name': 'Aman', 'country': 'USA'}
# (existing value kept, no overwrite!)


# Example 3: Using setdefault() with missing key (no default provided)
person = {"age": 25}
print(person.setdefault("city"))   # OUTPUT → None
print(person)
# OUTPUT → {'age': 25, 'city': None}
