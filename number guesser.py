from random import *

comp_number = randint(1, 100)

number_guess = input("Enter your guess:")
intnumber_guess = int(number_guess)
i = 0
for i in range(6):
    if(comp_number==intnumber_guess):
        print("correct")
        break 
    elif(comp_number>intnumber_guess):
        print("your number too small")
        i +=1
        number_guess = input("Enter your guess:")
        intnumber_guess = int(number_guess)
    else:
        print("your nunmber too big")
        number_guess = input("Enter your guess:")
        intnumber_guess = int(number_guess)
        i+=1

if (i==6):
    print("you ran out of guesses, the correct number was " +str(comp_number))
