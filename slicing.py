# string[start:stop:step]
# start: The index where the slicing begins (inclusive).
# stop: The index where the slicing ends (exclusive).
# step: The step or increment between indices (default is 1).
# Original string
text = "Hello, World!"

# Slicing from index 0 to 5 (excluding 5)
result1 = text[0:5]
print(result1)  # Output: Hello

# Slicing from index 7 to the end of the string
result2 = text[7:]
print(result2)  # Output: World!

# Slicing from the beginning to index 5 (excluding 5)
result3 = text[:5]
print(result3)  # Output: Hello


# negative indexex
# Original string
text = "Python is awesome!"

# Slicing the last 6 characters
result4 = text[-6:]
print(result4)  # Output: some!

# Slicing from index -13 to -9 (excluding -9)
result5 = text[-13:-9]
print(result5)  # Output: is a



# using step
# Original string
text = "abcdefghij"

# Slicing with a step of 2
result6 = text[1:8:2]
print(result6)  # Output: bdfh

# Reversing a string using step -1
result7 = text[::-1]
print(result7)  # Output: jihgfedcba


# Omitting Start, Stop, and Step:
# Original string
text = "Programming"

# Slicing the entire string (start, stop, and step omitted)
result8 = text[:]
print(result8)  # Output: Programming

# Same as result8, but with step omitted (defaults to 1)
result9 = text[::]
print(result9)  # Output: Programming


# Keep in mind that when using string slicing, the original string remains unchanged.
#  Slicing creates a new string based on the specified indices. Additionally, it's important to handle indices carefully to avoid IndexError.





