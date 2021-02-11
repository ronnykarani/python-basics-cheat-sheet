#***************************#
#GUESSING GAME
#built using a while loop
#you have 3 chances to make a correct guess
#hidden number is 9
#if the user makes a correct guess terminate the while loop
#***************************#


#define a variable to store the secret number
secret_number = 9
#number of guesses the user has to make
guess_count = 0
#guess limit
guess_limit = 3

#the while condition below will be executed tocompletion if the user cannot guess the number ...BUT upto where the condition becomes false 
while  guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won")
        break
    #this if has no else part
else:#this code will be executed if the while loop completes successfully without an immediate break
    print("Sorry you failed")