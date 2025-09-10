# 🐍 Palindrome Program
# ───────────────────────────────────────────────
# ✅ Palindrome = A string/number that reads the same
#    forward and backward.
# Examples: "madam", "121", "racecar"


# 🔹 Method 1: Using String Slicing
def is_palindrome(text):
    if text == text[::-1]:       # reverse the string using slicing
        return True
    else:
        return False


# Test
print(is_palindrome("madam"))    # OUTPUT → True
print(is_palindrome("hello"))    # OUTPUT → False



# 🔹 Method 2: Ignoring Case & Spaces (better)
def clean_palindrome(text):
    text = text.replace(" ", "").lower()  # remove spaces & lowercase
    return text == text[::-1]


print(clean_palindrome("RaceCar"))        # OUTPUT → True
print(clean_palindrome("Never odd or even"))  # OUTPUT → True



# 🔹 Method 3: Palindrome Check for Numbers
def is_num_palindrome(num):
    return str(num) == str(num)[::-1]     # convert number → string → check

print(is_num_palindrome(121))    # OUTPUT → True
print(is_num_palindrome(123))    # OUTPUT → False
