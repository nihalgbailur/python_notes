# # In Python, operators are symbols that perform operations on variables and values. They are classified into different types based on the operations they perform. Here are some common types of operators in Python:

# # 1. **Arithmetic Operators:**
# #    - Perform basic arithmetic operations.
# #    - Examples:
# #      ```python
# a = 10
# b = 5
# addition = a + b      # 15
# subtraction = a - b   # 5
# multiplication = a * b # 50
# division = a / b       # 2.0 (float result)
# modulus = a % b        # 0 (remainder)
# exponentiation = a ** b  # 100000

# # 2. **Comparison Operators:**
# #    - Compare two values and return a Boolean result (True or False).
# #    - Examples:
# #      ```python
# x = 10
# y = 20
# equals = x == y       # False
# not_equals = x != y   # True
# greater_than = x > y  # False
# less_than = x < y     # True


# 3. **Logical Operators:**
#    - Combine multiple conditions and return a Boolean result.
#    - Examples:
#      ```python
#      p = True
#      q = False
#      logical_and = p and q    # False
#      logical_or = p or q      # True
#      logical_not = not p      # False
#      ```

# 4. **Assignment Operators:**
#    - Assign values to variables.
#    - Examples:
#      ```python
#      x = 5
#      x += 3  # Equivalent to x = x + 3
#      x -= 2  # Equivalent to x = x - 2
#      ```

# 5. **Bitwise Operators:**
#    - Perform bit-level operations.
#    - Examples:
#      ```python
#      a = 5   # Binary: 0101
#      b = 3   # Binary: 0011
#      bitwise_and = a & b   # 1 (Binary: 0001)
#      bitwise_or = a | b    # 7 (Binary: 0111)
#      ```

# 6. **Membership Operators:**
#    - Test whether a value is a member of a sequence (e.g., a list, tuple, or string).
#    - Examples:
#      ```python
#      my_list = [1, 2, 3, 4]
#      is_member = 3 in my_list  # True
#      not_member = 5 not in my_list  # True
#      ```

# 7. **Identity Operators:**
#    - Compare the memory address of two objects.
#    - Examples:
#      ```python
#      a = [1, 2, 3]
#      b = [1, 2, 3]
#      identity_check = a is b        # False (different objects)
#      not_identity_check = a is not b  # True
#      ```

# # **Operator Precedence:**
# # Operator precedence determines the order in which operations are performed. Operators with higher precedence are executed first. Here is a general order of precedence (from highest to lowest) for some common operators:

# # 1. Parentheses `()`
# # 2. Exponentiation `**`
# # 3. Unary plus `+`, unary minus `-` (e.g., `-x`)
# # 4. Multiplication `*`, division `/`, modulus `%`
# # 5. Addition `+`, subtraction `-`
# # 6. Bitwise shift operators `<<`, `>>`
# # 7. Bitwise AND `&`
# # 8. Bitwise XOR `^`
# # 9. Bitwise OR `|`
# # 10. Comparison operators (`<`, `<=`, `>`, `>=`, `==`, `!=`)
# # 11. Logical NOT `not`
# # 12. Logical AND `and`
# # 13. Logical OR `or`

# Parentheses can be used to override the default precedence and force a specific order of operations. For example:
# ```python
# result = (a + b) * c
# ```

# This ensures that the addition operation (`+`) is performed before the multiplication (`*`).