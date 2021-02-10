#******PYTHON CHEAT SHEET******#

#**************************
#PRINTING TEXT
#built in function print() is used
#python interprator executes line of code line by line from the top
print('Hello Ronny')
print("Ronny Karani")
print('o----')
print(' ||||') #Quotes define a string of characters
#**************************


#**************************
#SAMPLE OPERATIONS
#Expression in python produces a value
#integrs(int) are numbers with no decimal points
#floats are numbers with decimal points
print('?' * 10) 
print(2 *3)
print(8//2)
print(18%4)
print(2*4+5-2)
print(2*(3+4))
print((4+8)/2)
print(3/4)
print(6*7.0)
print(4+1.655)
print(2**3)
#**************************


#**************************
#VARIABLES
#Identifier is the name of the variable used to identify the variable
#Variables are used to temporarily store data
#Allow you to store a value by assigning it to a name
#simple values stored in the variable include int..floats..strings..booleans
#The value can be used to refer to the value later in the program
one_price = 10
#python interprator allocates some memory to the price and stores 10 in it
#Therefore the price can be refered to at any point to access the stored value
one_price = 20
one_rating = 9.5
one_name = 'Kanana'
#undesrscores(_) are used to separate multiple words in avariables name
#True/False are boolean values
#python is case sensitive for special key words e.g Booleans
is_published = True
print(one_price)
#**************************
#**************************
#QUIZ
#Check in a patient named John Smith.
#20yrs old and is a new patient 
#--Define 3 variables for name, age and to check if heis a new patient/Existing patient
full_name = 'John Smith'
his_age = 20
is_new = True
#**************************


#**************************
#GETTING INPUT FROM THE USER AND CONCATENATION
#Built in function input() is used
name = input('What is your name? ')
#input function returns whatever the user enters
#returned value can the be stored in a variable
#thru joining/concatenation of the strings and  variables,we can print out an output
print('Hi ' + name)
#hi is concatenated/ joined with the variable
#take note of the white space in the strings to have a better output
#**************************
#**************************
#QUIZ
#Ask two questions name and favorite color and print a message 'name likes color'
new_name = input('What is your name? ')
new_color = input('What is your favorite color? ')
print(new_name + ' likes ' + new_color)
#**************************


#**************************
#TYPE CONVERSION
#NB input will always be treated as a string
#strings can be concatenated together
#to carry operations on integers ,strings or floats one has to be converted to the others type
#program that asks for our year of birth, calculates your and prints out our age
#gets the year of birth and stores it in a variable
age = ()
birth_year = input('Year of Birth: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age) 
#**************************
#**************************
#QUIZ
#As user their weight in pounds convert it to kilograms and print on the terminal
kgs = ()
your_weight = input('Whats your weight in pounds: ')
print(type(your_weight))
kgs = int(your_weight) * 0.453592
print(type(kgs))
print(kgs)
#**************************


#**************************
#STRINGS 
#Defined by quotes both single and double
course = 'Python for beginners'
print(course)
#Using quotes in the string might result to it ending prematurely
#hence need to escape the string with a backslash or use othe quotes
course = 'Python\'s for beginners'
course = "Python\'s for beginners"
course = 'Python for "beginners"'
print(course) 
message = '''
Hi Ron 
Here is our offer
Thank you,
Management
'''
print(message)
#to get characters at a given index in the string we use []
#pyhton uses zero indexing
# 0 is the index of the first charcater
look = 'ronny karani'
print(look[4])
#NB the space will also be indexed
#Using a negative index will give us the characters starting from the end
# -1 will be the index of last character
look_one = 'ronny karani'
print(look_one[-3])
#using the square brackets to extract a range of characters
#add : btwn the range (starting from the fast to the second)
#the character in the second index is not returned
print(look_one[3:8])






