# 🔹 1. *args (variable-length positional arguments)
def add_numbers(*args):           # collects arguments into a tuple
    return sum(args)

print(add_numbers(1, 2, 3))       # OUTPUT → 6
print(add_numbers(10, 20, 30, 40))# OUTPUT → 100


# 🔹 2. **kwargs (variable-length keyword arguments)
def print_details(**kwargs):      # collects arguments into a dictionary
    for key, value in kwargs.items():
        print(key, ":", value)

print_details(name="Aman", age=25, city="Bangalore")
# OUTPUT →
# name : Aman
# age : 25
# city : Bangalore
