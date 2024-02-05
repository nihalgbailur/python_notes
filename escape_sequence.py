# Escape sequences in programming languages, including Python, are sequences of characters that represent special meanings and are used to perform various tasks, such as formatting output, including special characters, and more. In Python, escape sequences are preceded by a backslash (`\`). Here are some common escape sequences in Python:

# 1. **`\n` - Newline:**
#    - Moves the cursor to the beginning of the next line.
#    ```python
#    print("Hello\nWorld")
#    # Output:
#    # Hello
#    # World
#    ```

# 2. **`\t` - Tab:**
#    - Inserts a tab character, aligning text at tab stops.
#    ```python
#    print("Hello\tWorld")
#    # Output:
#    # Hello   World
#    ```

# 3. **`\r` - Carriage Return:**
#    - Moves the cursor to the beginning of the current line.
#    ```python
#    print("Hello\rWorld")
#    # Output:
#    # Worldlo
#    ```

# 4. **`\\` - Backslash:**
#    - Represents a literal backslash.
#    ```python
#    print("This is a backslash: \\")
#    # Output:
#    # This is a backslash: \
#    ```

# 5. **`\'` and `\"` - Single and Double Quotes:**
#    - Represent single and double quote characters within a string.
#    ```python
#    print('He\'s a programmer.')
#    # Output:
#    # He's a programmer.
#    ```

#    ```python
#    print("She said, \"Hello.\"")
#    # Output:
#    # She said, "Hello."
#    ```

# 6. **`\b` - Backspace:**
#    - Moves the cursor back one space.
#    ```python
#    print("Hello\bWorld")
#    # Output:
#    # HellWorld
#    ```

# 7. **`\f` - Form Feed:**
#    - Moves the cursor to the next page or form.
#    ```python
#    print("Hello\fWorld")
#    # Output:
#    # Hello
#    #      World
#    ```

# 8. **`\u` and `\U` - Unicode Escapes:**
#    - Represents a Unicode character using hexadecimal (4 digits) or Unicode code point (8 digits).
#    ```python
#    print("\u03A9")  # Greek capital letter omega
#    # Output: Ω
#    ```

#    ```python
#    print("\U0001F609")  # 😊 (smiling face with smiling eyes)
#    ```

# These escape sequences are helpful for controlling the formatting and appearance of strings in your Python programs.
def print_with_escape_sequences():
    print("Hello\nWorld")
    print("Hello\tWorld")
    print("Hello\rWorld")
    print("This is a backslash: \\")
    print('He\'s a programmer.')
    print("She said, \"Hello.\"")
    print("Hello\bWorld")
    print("Hello\fWorld")
    print("\u03A9")  # Greek capital letter omega
    print("\U0001F609")  # 😊 (smiling face with smiling eyes)

# Call the function to see the output
print_with_escape_sequences()
