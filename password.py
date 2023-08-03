"""Code to generate a password with user preferences"""
import random
from random import choice   
import string

length = input("How long do you want your password to be? ")
numbers = input("Max amount of numbers in your password? ")
specialChar = input("Max amount of special characters you want(ex: {, ], !, }, etc)? ")
int_numbers= int(numbers)
int_specialChar= int(specialChar)
password = ""


for i in range(int(length)):
    randomLetter = random.choice(string.ascii_letters)

    num = random.randint(0,100)

    if(num %2==0):
        password += randomLetter

    if (int_numbers !=0):
        if(num%6==0):
                int_numbers-=1
                digits = random.choice(string.digits)
                password += str(digits)

    elif (int_specialChar!=0):
        if(num%6==0):
            int_specialChar-=1
            chars = random.choice(string.punctuation)
            password+=chars


while len(password) < int(length):
    randomLetter = random.choice(string.ascii_letters)
    password += randomLetter.lower()

print(password)