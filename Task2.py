#Calculations using maths module
import math
def operations():
    try:
        n = input("Enter a number: ")
        n = float(n)
    except ValueError:
        return "Invalid input. Please enter a valid number."
    # Calculate square root
    math.square_root = math.sqrt(n)
    print(f"Square root of {n} is: {math.square_root}")
    # Calculate natural logarithm
    if n <= 0:
        print("Natural logarithm is not defined for non-positive numbers.")
        return
    print(f"Natural logarithm of {n} is: {math.log(n)}")
    # Calculate sine
    math.sine = math.sin(n)
    print(f"Sine of {n} is: {math.sine}")

operations()
