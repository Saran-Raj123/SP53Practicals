"""
CP1404/CP5632 - Practical - Saranraj Saravanan
Answer the following questions:
1. When will a ValueError occur?
# A ValueError will occur if the user enters a value that cannot be converted to an integer when using int(input(...)). For example, if the user enters a string or any non-numeric input.
2. When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur if the user enters a denominator of 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check if the denominator is zero before entering division
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers.txt!")

print("Finished.")
