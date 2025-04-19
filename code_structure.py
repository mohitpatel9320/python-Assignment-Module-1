# Program to calculate the area of a circle
# Demonstrates basic Python code structure

# 1. Import Statements
import math  # Importing math module to use pi and power functions

# 2. Global Variables / Constants
PI = math.pi  # Using the pi constant from the math module

# 3. Input Section
radius = float(input("Enter the radius of the circle: "))  # Taking user input

# 4. Calculation Section
circle_area = PI * radius ** 2  # Formula: πr²

# 5. Output Section
print(f"The area of the circle with radius {radius} is {circle_area:.2f}")