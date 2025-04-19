# Program to filter out even numbers using the filter() function

def is_odd(number):
    return number % 2 != 0

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter to get only odd numbers
odd_numbers = list(filter(is_odd, numbers))

print("Odd numbers:", odd_numbers)