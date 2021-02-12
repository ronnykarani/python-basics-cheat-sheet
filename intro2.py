#******************************#
#******PYTHON CHEAT SHEET******#
#******************************#

#******************************
#WHILE LOOPS
#while loops are use to execute a block of code multiple times
#Syntax = while condition:
#if the condition is true the code below that will be repeatedly executed
#when the condition evaluates tofalse it jumps out of the loop
index = 1
while index <= 5:
    print(index)
    index += 1 #increases the index by one on every iteration to avoid an infinite loop
print("Done")

i = 1
while i <= 5:
    print('*' * i)
    i += 1 
print("Done")
#break and continue statements
#break stops the loop from iterating again(ends the loop prematurely)
#continue stops the current loop/iteration and goes to the next one
#****************************


#****************************
#FOR LOOPS
#used to iterate over items of a collection e.g string
#a loop variable is defined and in each iteration it will hold one item in each
for item in 'Python':
    print(item)

#can also be used in a range function
#when the range function is called it creates an object that we caniterate over
for item in range(10):
    print(item)
#the could also be given limits
for items in range(5,10):
    print(items)
#steps can be used to give the range iteration steps
for items in range(5,10,2):
    print(items)
#************************************
#QUIZ
#a for loop to calculate total cost of items in a shopping cart
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")
#*******************************


#*******************************
#NESTED LOOPS
#nested loop involves adding a loop inside another loop
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
#*******************************
#QUIZ
#using nested loops draw F on your console
numbers = [5, 2, 5, 2, 2]

for num in numbers:
    #print('x' * num)
    output = ''
    for count in range(num):
        output += 'x'
    print(output)
#********************************



#********************************
#LISTS
names = ['john', 'bob', 'mosh', 'joan']
print(names)
#individual names in a list can be accessed
#accessed by indexing using []
print(names[2])
print(names[-1])
#negative index will start from the end of the list
#ranges of items in the list can be selected by using :
#range could be specified with an end index, steps can also be added or even left blank
#python interprator knows what to do in such cases
print(names[1:3])
print(names[2:])
print(names[:2])
print(names[:])
#the square brackets do not modify the original list they simply return a new list
#modifying items in a list 
#access the list via the index and modify
names[0] = 'jon'
print(names)
#******************************
#QUIZ
#Program to find the largest number in a list
numerals = [3, 6, 2, 8, 4, 10]
max = numerals[0]
for number in numerals:
    if number >max:
        max = number
print(max)
#*****************************


#*****************************
#2D LISTS
#involves each item in the list being another list
#that list reps items in each row
#square brackets are used to access the items via indexing
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][2] = 20
print(matrix[0][1])
#nested loop could be used to iterate over all the items in the matrix
for row in matrix:
    for item in row:
        print(item)
#******************************


#******************************
#LIST METHODS[]
#operations that can be performed on the list
digits = [3, 5, 7, 1, 8, 4, 6]
#add a number at he end of the list
digits.append(9)
print(digits)
#add a number anywhere on the list using index as first argument and the new number as second
digits.insert(0, 2)
print(digits)
#remove an item from the list
digits.remove(5)
print(digits)
#to reemove the last item in a list
digits.pop()
print(digits)
#to check index of an item from the list
digits.index(3) 
print(digits)
#To clear all the items from the list
digits.clear()
print(digits)
#using the in operator to check for the existence of an item in a list
name = ['jon', 'allan', 'lewis', 'ann', 'jon']
print('allan' in name)
#returns a boolean value
#counting same items in the list/check how many times they occur
name = ['jon', 'allan', 'lewis', 'ann']
print(name.count('jon'))
#sort method is used to sort the list
#None is an object in python that reps the abscence of a value
name = ['jon', 'allan', 'lewis', 'ann']
name.sort()
name.reverse()#used to reverse the order
print(name)
#items will be sorted in ascending order
#to get a copy of the list ..copy method is used
#second list will not be affected by any changes we make there after
numbers1 = [1,4,5,3,7,8,9,2,10]
numbers2 = numbers1.copy()
numbers1.append(13)
print(numbers1)
print(numbers2)
#*********************************
#QUIZ
#remove duplicates in a list
nums =[2,2,4,6,3,6,1]
uniques=[]
for num in nums:
    if num not in uniques:
        uniques.append(num)
print(uniques)
#*********************************


#*********************************
#TUPLES()
#similar to list
#can be used to store a list of items
#unlike lists tuples cannot be modified
#they imutable, cannot mutate or change
#from the tuple you can only get info about an item
#count used to count number of occurences of an item
#index used to find index of the first occurence of an item
new_numbers = (1, 2, 3)
print(new_numbers[1])
#***********************************


#***********************************
#UNPACKING
#used in both tuples and lists
#assigns the items in the tuple => unpacking the tuple
coordinates = (1,2,3)
x,y,z = coordinates
print(x,y,z)

coordinates_new = [1,2,3]
x,y,z = coordinates_new
print(x,y,z)
#************************************


#************************************
#DICTIONARIES{}
#used to store info as key-value pairs
# key : value
#value can be anything ...int,str,boolean,list
#values in the dictionary can be accessed [] or the get method
#case sensitive on the sequence of characters
customer = {
    "name": "John Smith",
    "age": 25,
    "is_verified": True
}
customer["name"]
customer["age"]
print(customer.get("name"))
#if the dictionary has no value key you can supply a default
print(customer.get("birthdate", "Jan 1 1980"))
#NB in and not in can alsobe used to determine if a key value is contained in the dictionary
#************************************
#QUIZ
#program that asks for our phone number in digits and returns it in words
phone  = input("Phone: ") 
digits_map = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}
output = ""
for char in phone:
    output += digits_map.get(char, "!") +  ""
print(output)
#**************************************


#**************************************
#EMOJI CONVERTER IN A DICTIONARY
#dictionary that maps characters to smiley faces
#the split method is used to divide input into separate words
#the split method will return a list
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "👍",
    ":(" : "👎"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
#*************************************
