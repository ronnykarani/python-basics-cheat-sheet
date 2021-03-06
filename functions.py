#******************************#
#******PYTHON CHEAT SHEET******#
#******************************#

#******************************#
#FUNCTIONS
#Functions are containers that perform a specific task 
#Functions are reusable, manageable and maintainable chunks of code
#def is a reserve keyword used to define a function...its then followed by the function name
#naming rules in variables also apply here
#PEP advices adding two lines of whitespace after defining a function
def greet_user():
    print('hi there')
    print('welcome aboard')
    
    
print('Start')
greet_user()  
print("Finish")
#lines of code in the function will only get xecuted when we call the function  
#***************************************


#**************************************
#PARAMETERS
#**************************************
#parameters can be added to functions and they act as placeholders for receiving info
#Eg you can add the name as a parameter and call the name when calling the function ...acts a positional argument
#argument is the value supplied to a function
#tamia and abade are arguments passed to the name parameter
def greet_user(name):
    print(f'hi {name}')
    print('welcome aboard')
    
    
print('Start')
greet_user("Tamia")  
greet_user("Abade") 
print("Finish") 


def greet_user(first_name, last_name):
    print(f'hi {first_name} {last_name}')
    print('welcome aboard')
    
    
print('Start')
greet_user("Tamia", "Abade")   
print("Finish") 
#************************************


#**************************************
#KEYWORD ARGUMENTS
#**************************************
#Whenever you define parameters always pass some values/arguments
#positional arguments should match their specific parameter
def greet_user(first_name, last_name):
    print(f'hi {first_name} {last_name}')
    print('welcome aboard')
    
    
print('Start')
#incase positional arguments do not match the parameters...keyword argument is used
#prefix each value with the name of the parameter they target
greet_user(last_name="Abade" ,first_name="Tamia")   
print("Finish") 
#keyword arguments increase readability of numerical values
#when using both positional and keyword arguments always use positional arguments first
#************************************************


#************************************************
#RETURN STATEMENT
#************************************************
def square(number):
    return number  * number


print(square(3))
#by default all function statements return none which is the absence of a value
#*************************************************


#**************************************************
#CREATING A REUSABLE FUNCTION
#**************************************************
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "👍",
        ":(" : "👎"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
#*************************************************


#*************************************************
#EXCEPTION HANDLING
#*************************************************
#try the code will try and run the code
#except handles the error  expected from the code
#different exception catch different types of errors
try:
    age = int(input('age:'))
    print(age)
except ValueError:
    print('invalid value')
#*************************************************


#************************************************
#COMMENTS
#************************************************
#used to add comments 


#***********************************************
#CLASSES
#classes are used to define new types to modelreal concepts
#convention used in naming classes(Pascal) is different from variables and functions
class Point:
    def move(self):
        print('move')
        
    def draw(self):
        print('draw')


point1 = Point()
point1.x= 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x= 10
point2.y = 20
print(point1.x)
point1.draw()
#***********************************************


#***********************************************
#CONSTRUCTORS
#***********************************************
#A function that gets called at the time when creating an object
class Point:
    #the init method gets called when we create a new point object
    def __init__(self, x, y):#this methods constructs/creates an object
        self.x = x#initializing the object
        self.y = y#self acts as a reference to the  current object
        
    def move(self):
        print('move')
        
    def draw(self):
        print('draw')
        

point = Point(10,20)
point.x = 11 #updates value
print(point.x)


class Person:#define the person class
    def __init__(self, name):
        self.name = name#self refernces the current object
    #above code sets the name attribute of  the current object to the name argument passed
    def talk(self):#with this self we can get reference tothe current object 
        print(f'Hi, I am {self.name}')


john = Person("john smith")
john.talk()

bob = Person("bob smith")
bob.talk() 
#each object is a different instance of a person class  
#***********************************************


#**********************************************
#INHERITANCE
#*********************************************
#is a mechanism for re-using code
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print("woof")


class Cat(Mammal):
    def purr(self):
        print("meow")


dog1 =Dog()
dog1.bark()

cat1 =Cat()
cat1.purr()
#******************************************