#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side1, side2
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704
import math
side1 = float(input("Enter the value for side1"))
side2 = float(input("Enter the value for side2"))

hypotenuse = str(math.sqrt(side1 ** 2 + side2 ** 2))

print("The hypotenuse of the right triangle is " + hypotenuse + ".")