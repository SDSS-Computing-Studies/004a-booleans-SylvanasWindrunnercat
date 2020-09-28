#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
a = input("The number is:")

a = float(a)

if a == int(a):
    print("The number is an integer")
else:
    print("Then number is not an integer")
