#! python3

# Have the user enter in a sentence. 
# Check to see if the word "password" is located in the sentence

# Inputs:
# a sentence

# Outputs:
# "the sentence contains password"
# "the sentence does not contain password"
a = input("The sentence is:")

b = "password"

if b in a:
    print("The sentence located password")
else:
    print("The sentence doesn't located password")