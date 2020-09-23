#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

a = float(input("Enter the a value"))
b = float(input("Enter the b value"))
c = float(input("Enter the c value"))

x = str((c-b) / a)
print("The x value is " + x + ".")