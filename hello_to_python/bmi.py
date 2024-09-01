#!/usr/bin/env python3

# BMI = (weight in kg / height in meters squared )

# gather information from user
def gather_information():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    return weight, height

# calculate BMI
def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: weight / height^2
    """
    return weight / (height ** 2)

while True:
    weight, height = gather_information()
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

    # ask user if they want to calculate again
    again = input("Do you want to calculate again? (y/n): ")
    if again.lower() != 'y':
        break