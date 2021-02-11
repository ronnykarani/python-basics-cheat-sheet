#******************************#
#******PYTHON CHEAT SHEET******#
#******************************#


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
#always use meaningful names for your variables
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
#if you dont key in the end index python returns all characters to the end of the string
print(look_one[3:])
#if you dont key in the start index python takes it as a zero and returns characters from the zero index 
print(look_one[:3])
#if both index are left blank python takes the first index as a zero and go all the way to end
#its just like copying the whole string
another = look_one[:]
print(another)

new_name = 'joan kanana'
print(new_name[1:-1]) 
#NB when you multiply a string by a number the string will be repeated those number of time
print("ron" * 5)
#empty strings have no characters
print('')
#**************************


#**************************
#FORMATTED STRINGS
#Useful where you want to generate dynamic text with variables
first_name = 'john'
last_name = 'smith'
message = first_name + ' [' + last_name + '] is a coder '
print(message)
#above code is not ideal for complicated texts since it becomes harder to visaulize the output
#there is where formatted strings come in handy
#formatted strings are prefixed with an f
msg =  f'{first_name} [{last_name}] is a coder'
#{} define placeholders/holds in our strings
#holds will be filled by values of our variables when we run the program
print(msg)
#**************************


#**************************
#STRING METHODS
lesson = 'Python For Beginners'
#len is used to calculate the length of the variable
print(len(lesson))
#white spaces will also be treated as characters
#len function can be used to enforce a limit on the number of characters 
#len is a general purpose function 

#other functions are only specific to strings also known as methods
# eg  upper and lower
#when a function is specific to an object we refer to it as method
#upper and lower are methods since the belong to the string unlike len and print 
#to access this functions we use the dot operator(.)
#.upper and .lower converts the string to either of the cases
print(lesson.upper())
print(lesson.lower())
#the method upper does not modify our string it just creates a new string and returns it
print(lesson)
# title method is used toconvert the first character in each word to uppercaseand remaining characters to lowercase
#title method just like upper and lower returns a new string
my_title = 'the lion is out'
print(my_title.title())
print(my_title)

#finding a sequence of characters in a string
#the find method is used
#find method is case sensitive
#when a character thats not in the string is passed a negative will be returned
lesson = 'Python For Beginners'
print(lesson.find('P'))
print(lesson.find('g'))
print(lesson.find('O'))
print(lesson.find('Python'))
print(lesson.find('Beginners'))
#find will return the index of the first appearance of the defined character in the string
#if a sequence is passed find method will return the first index, where the sequence starts

#replace method is used to replace characters in the string
#the method will take two arguments (character to replace, new character)
print(lesson.replace('Beginners','Absolute Beginners'))
#the method is also case sensitive
print(lesson.find('P','J'))

#another sequence is to check existence of a character or sequence in a string
#in operator is used
#in operator is a boolean expression since it returns either true or false
my_name = 'Ronny Karani Mwirigi'
print('Ronny' in my_name)
print('ronny' in my_name)
#in operator is also is also case sensitive
#**************************


#**************************
#ARITHMETIC OPERATIONS
#addition
print(10 + 2)
#subtraction
print(10 - 2)
#multiplication
print(10 * 2)
#division
#gets a float(/) 0r an intrger(//)
print(10 / 3)
print(10 / 2)
print(10 // 3)
print(10 // 2)
#modulus(gets remainder of the division)
print(10 % 3)
#exponent(power)
print(10 ** 3)

#augmented sign operators/In-place operators
# = is an assignment operator
x = 10
x = x + 3
print(x)
#above operation is simplified by augmentation
y = 10
y += 3
print(y)
#augmented assign operator can be used in other arithmetic operation(-, *, / ..etc)
z = 10
z -= 3
print(z)
#******************************


#******************************
#OPERATOR PRECEDENCE
#some operators have a higher precedence compared to others
a = 10 + 3 * 2
print(a)
# order fom the highest precedence exponentiation, multiplication or division, addition or subtraction
b = 10 + 3 * 2 ** 2
print(b) 
#parentheses can be used to change the order of opeeration
#parentheses will always take the first priority
c = (10 + 3) * 2 ** 2
print(c) 
#*************************


#*************************
#MATH OPERATIONS
#rounding the nummber
#to round a number you can use a built in function called round
d = 2.7
print(round(d))
#abs for absolute value always return the positive value
e = -3.5
print(abs(e))
#other math operations (complex) can be carried out by importing amath module
#a module is a separate file with reusable code
import math 
print(math.ceil(2.8))
print(math.ceil(2.3))
#ceil returns the next whole number
print(math.floor(2.8))
print(math.floor(2.3))
#floor will return the previous whole number
#************************


#************************
#IF STATEMENTS
#Allow building of programs that can make decisions based on some conditions
#if a condition is true do sth otherwise do sth else
#if statemnets should be indented
is_hot = False #could be true or false
is_cold = True #could be true or false

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a cold day")

print("ENJOY YOUR DAY") 
#if statements can be used to build rules into the program
#********************************
#QUIZ
#Price of a house is $1M
#If buyer has good credit they need to put down 10%
#otherwise the need to put down 20%
#Write a program with this rules and display thre down payment required
#for a buyer with good credit
price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price 
else:
    down_payment = 0.2 * price 
print(f"Down payment: ${down_payment}")
#************************


#************************
#LOGICAL OPERATORS
#used in situations with multiple conditions
# AND  used to combine both conditions
#requires both conditions to evaluate to true
high_income = True
has_good_credit = True

if high_income and has_good_credit:
    print("Eligible for loan")

# OR used to check if either of the conditions is true
#requires one condition to be true
high_salary = True
has_better_credit = False

if high_salary or has_better_credit:
    print("Eligible for loan")

#NOT inverses boolean value
#true to false and vice versa
has_nice_credit = True
has_criminal_record =  False

if has_nice_credit and not has_criminal_record:
    print("Eligible for loan")
#******************************


#******************************
#COMPARISON OPERATORS
#used to compare two or more values
# greater than >
#less than <
#equal to == (equality operator)
#not equal !=
#greater than or equal to >=
#less than or equal to <=
temp = 30

if temp > 30:
    print("Hot day")
else:
    print("Not hot")
#*************************
#QUIZ
#if name is less than 3 characters long return name should be atleast 3 characters wrong
#otherwise if it is more than 5o characters long name cannot be a max of 50 characters
#otherwise name looks good
name = "John"

print(len(name))
if len(name) < 3:
    print("Name must be atleast three charactres")
elif len(name) > 50:
    print("Name should not be more than fifty character")
else:
    print("Name looks good")
#*******************************