"""Code to generate a password with user preferences"""
import random
import string

length = input("How long do you want your password to be? ")
numbers = input("How many numbers do you want? ")
specialChar = input("How many special characters do you want(ex: {, ], !, }, etc)? ")
numbers= int(numbers)
specialChar= int(specialChar)
password = ""

for i in range(int(length)):
    randomLetter = random.choice(string.ascii_letters)
    num = random.randint(0,10)
    if(num%4==0):
        randomLetter= randomLetter.upper()

    if (numbers !=0):
        numbers-=1
        digits = random.choice(string.digits)

    if(specialChar!=0):
        specialChar-=1
        chars = random.choice(string.punctuation)

    
    password += randomLetter
    

print(password)