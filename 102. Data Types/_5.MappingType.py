# 🐍 Python Mapping Type → Dictionary
# ───────────────────────────────────────────────
# ✅ Dictionary (dict):
# - Stores data as key–value pairs.
# - Keys must be unique & immutable (string, number, tuple).
# - Values can be any type (int, str, list, dict, etc.).
# - Mutable & ordered (since Python 3.7).

# 🔹 Creating a Dictionary
student = {"name": "Aman", "age": 25, "skills": ["Python", "DSA"]}
print(student)
# OUTPUT → {'name': 'Aman', 'age': 25, 'skills': ['Python', 'DSA']}


# 🔹 Accessing Values
print(student["name"])             # OUTPUT → Aman
print(student.get("age"))          # OUTPUT → 25
print(student.get("city", "NotFound"))   # OUTPUT → NotFound (default used)


# 🔹 Adding / Updating
student["city"] = "Bangalore"      # Add new key
student["age"] = 26                # Update value
print(student)
# OUTPUT → {'name': 'Aman', 'age': 26, 'skills': ['Python', 'DSA'], 'city': 'Bangalore'}


# 🔹 Removing
student.pop("skills")              # remove by key
print(student)
# OUTPUT → {'name': 'Aman', 'age': 26, 'city': 'Bangalore'}

del student["city"]                # delete by key
print(student)
# OUTPUT → {'name': 'Aman', 'age': 26}

student.clear()                    # empty dictionary
print(student)
# OUTPUT → {}


# 🔹 Dictionary Methods
person = {"name": "Aman", "age": 25, "city": "Delhi"}

print(person.keys())     # OUTPUT → dict_keys(['name', 'age', 'city'])
print(person.values())   # OUTPUT → dict_values(['Aman', 25, 'Delhi'])
print(person.items())    # OUTPUT → dict_items([('name', 'Aman'), ('age', 25), ('city', 'Delhi')])

# Iterating
for key, value in person.items():
    print(key, ":", value)
# OUTPUT →
# name : Aman
# age : 25
# city : Delhi
