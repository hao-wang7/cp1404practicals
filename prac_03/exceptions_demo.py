"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# Answers to questions:
# 1. When will a ValueError occur?
#    ValueError will occur if the user inputs something that can't be converted to an integer, such as letters, symbols, or decimal numbers.

# 2. When will a ZeroDivisionError occur?
#    ZeroDivisionError happens when the user enters 0 as the denominator, since dividing by zero is not allowed in mathematics.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#    Yes. To avoid a ZeroDivisionError, we can check if the denominator is zero before performing the division, and show an appropriate message instead of raising an exception.

# Modified code to avoid ZeroDivisionError
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check for zero denominator to avoid ZeroDivisionError
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")