# Program to demonstrate various string methods in Python

# Input string
input_string = "  Hello, Python Programming!  "

# 1. Strip whitespace from both ends
stripped_string = input_string.strip()
print(f"Stripped String: '{stripped_string}'")

# 2. Convert to uppercase
uppercase_string = stripped_string.upper()
print(f"Uppercase String: '{uppercase_string}'")

# 3. Convert to lowercase
lowercase_string = stripped_string.lower()
print(f"Lowercase String: '{lowercase_string}'")

# 4. Replace a substring
replaced_string = stripped_string.replace("Python", "Java")
print(f"Replaced String: '{replaced_string}'")

# 5. Split the string into a list
split_list = stripped_string.split()
print(f"Split List: {split_list}")

# 6. Join the list back into a string
joined_string = " ".join(split_list)
print(f"Joined String: '{joined_string}'")

# 7. Check if the string starts with a specific substring
starts_with_hello = stripped_string.startswith("Hello")
print(f"Starts with 'Hello': {starts_with_hello}")

# 8. Check if the string ends with a specific substring
ends_with_exclamation = stripped_string.endswith("!")
print(f"Ends with '!': {ends_with_exclamation}")

# 9. Find the position of a substring
position = stripped_string.find("Python")
print(f"Position of 'Python': {position}")

# 10. Count occurrences of a substring
count = stripped_string.count("o")
print(f"Count of 'o': {count}")