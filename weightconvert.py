#****************************#
# WEIGHT CONVERTER
# Program to take users weight in either pounds(lbs) or kilos(kgs) and convert
#the input to the other
#weight in kilos to pounds and vice versa
#***************************#


#Take the user input of both the weight and the weight unit
#store both inputs in a variable to be accesed later
#since the input always returns a string convert the weight to int 
#this will allow the conversion operation to take place
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

#Define the conditions
#conditions should not be case sensitive
#use upper method to ensure no matter the case the user uses it will go through
if unit.upper() == "L":
    convert = weight * 0.45
    print(f"You are {convert} kgs")
else:
    convert = weight / 0.45
    print(f"You are {convert} lbs")
















