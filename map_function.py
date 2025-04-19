# Program to square a list of numbers using the map() function

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Function to square a number
def square(num):
    return num ** 2

# Using map() to apply the square function to each element in the list
squared_numbers = list(map(square, numbers))

# Print the result
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)