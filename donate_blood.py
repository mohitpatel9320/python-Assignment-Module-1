# Program to check blood donation eligibility

# Input age and weight
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (in kg): "))

# Check eligibility using nested if
if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood because your weight is less than 50 kg.")
else:
    print("You are not eligible to donate blood because you are under 18 years of age.")