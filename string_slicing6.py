# Write a Python program to demonstrate string slicing.
# Example of string slicing
sample_string = "Hello, World!"

# Slicing to get "Hello"
part1 = sample_string[:5]

# Slicing to get "World"
part2 = sample_string[7:12]

# Slicing to get "Hello, World!"
full_string = sample_string[:]

# Slicing to get "World!" using negative indices
part3 = sample_string[-6:]

# Print the results
print("Original String:", sample_string)
print("Sliced Part 1:", part1)
print("Sliced Part 2:", part2)
print("Full String:", full_string)
print("Sliced Part 3:", part3)
