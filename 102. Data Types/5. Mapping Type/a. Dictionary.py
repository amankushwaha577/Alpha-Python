# 🐍 Python Dictionary Functions / Methods
# ───────────────────────────────────────────────
# ✅ Dictionaries store data as key–value pairs.
# ✅ Keys must be unique & immutable (str, int, tuple).
# ✅ Values can be of any type.
# ✅ Dictionaries are mutable (can add/remove/modify items).


# ⚡ Summary Table
# ───────────────────────────────────────────────
# Modifies Dict (in-place)   | update(), pop(), popitem(),
#                            | setdefault(), clear()
# ───────────────────────────|───────────────────────────────
# Does NOT Modify (returns)  | get(), keys(), values(), items(),
#                            | copy(), len(), min(), max(),
#                            | sorted()
# ───────────────────────────────────────────────

# ⚡ Quick Rule:
# - Methods that change/add/remove key–value pairs → modify dict.
# - Methods that fetch/query data → return values (don’t modify).


# ───────────────────────────────────────────────
# 🔹 METHODS THAT MODIFY THE DICT (in-place)
# ───────────────────────────────────────────────
student = {"name": "Aman", "age": 25}

# update(dict) → add or update multiple keys
student.update({"city": "Delhi", "age": 26})
print(student)
# OUTPUT → {'name': 'Aman', 'age': 26, 'city': 'Delhi'}

# pop(key) → remove key and return value
age = student.pop("age")
print(age)       # OUTPUT → 26
print(student)   # OUTPUT → {'name': 'Aman', 'city': 'Delhi'}

# popitem() → remove last inserted key–value pair
item = student.popitem()
print(item)      # OUTPUT → ('city', 'Delhi')
print(student)   # OUTPUT → {'name': 'Aman'}

# setdefault(key, default) → return value if exists, else add key
print(student.setdefault("country", "India"))
print(student)
# OUTPUT →
# India
# {'name': 'Aman', 'country': 'India'}

# clear() → remove all items
student.clear()
print(student)   # OUTPUT → {}


# ───────────────────────────────────────────────
# 🔹 METHODS / FUNCTIONS THAT DO NOT MODIFY
# ───────────────────────────────────────────────
person = {"name": "Aman", "age": 25, "city": "Delhi"}

# get(key, default) → safe access
print(person.get("age"))          # OUTPUT → 25
print(person.get("gender", "NA")) # OUTPUT → NA

# keys(), values(), items()
print(person.keys())    # OUTPUT → dict_keys(['name', 'age', 'city'])
print(person.values())  # OUTPUT → dict_values(['Aman', 25, 'Delhi'])
print(person.items())   # OUTPUT → dict_items([('name','Aman'),('age',25),('city','Delhi')])

# copy() → shallow copy
copy_dict = person.copy()
print(copy_dict)        # OUTPUT → {'name': 'Aman', 'age': 25, 'city': 'Delhi'}

# Built-in functions
print(len(person))      # OUTPUT → 3
print(sorted(person))   # OUTPUT → ['age', 'city', 'name'] (sorts keys alphabetically)
