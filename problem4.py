#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
a = input("The side1 is:")
b = input("The side2 is:")
c = input("The actual side is:")

a = float(a)
b = float(b)
c = float(c)

import math

d = math.sqrt (a**2 + b**2)

if 0 <= d - c <= 0.02:
    print("That is a right triangle")
elif d - c < 0:
    print("That is an acute triangle")
elif d - c > 0.02:
    print("That is an obtuse triangle")