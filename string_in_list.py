# Program to find a specific string in the list using a for loop and if condition

# List of strings
string_list = ["apple", "banana", "cherry", "date", "elderberry"]

# String to find
search_string = "cherry"

# Flag to check if the string is found
found = False

# Loop through the list
for string in string_list:
    if string == search_string:
        found = True
        break

# Output the result
if found:
    print(f"'{search_string}' is found in the list.")
else:
    print(f"'{search_string}' is not found in the list.")