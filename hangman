import requests
import random

print ("_________")
print ("|	 |")
print ("|")
print ("|")
print ("|")
print ("|")
print ("|________")
players = input("One player or two players?(Say 1 or 2): ")

if(int(players) == 2):
    word_input = input("Player 1, give me the word: ")
else:
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.decode('utf-8').splitlines()
    word_input = WORDS[random.randint(0, len(WORDS)-1)]

strVal = "_" * len(word_input)


failure = 0
while True:
    char_input = input(" guess a character:") 
    strVallist = list(strVal)

    locate = word_input.rfind(char_input)
    if(locate>=0):
        j = 0
        for i in range(len(word_input)):
             if word_input[i] == char_input:
                strVallist[i] = char_input           
        strVal = "".join(strVallist)

        print(strVal)

        if "_" not in strVal:
            print("Congratulations! You guessed the word!")
            break
            
        
    
    else:
        failure+=1
        if(failure == 1):
            print ("_________")
            print ("|	 |")
            print ("|")
            print ("|")
            print ("|")
            print ("|")
            print ("|________")
        elif (failure ==2):
            print ("_________")
            print ("|	 |")
            print ("|	 O")
            print ("|")
            print ("|")
            print ("|")
            print ("|________")
        elif(failure==3):
            print ("_________")
            print ("|	 |")
            print ("|	 O")
            print ("|	 |")
            print ("|	 |")
            print ("|")
            print ("|________")
        elif(failure ==4):
            print ("_________")
            print ("|	 |")
            print ("|	 O")
            print ("|	\|")
            print ("|	 |")
            print ("|")
            print ("|________")
        elif(failure==5):
            print ("_________")
            print ("|	 |")
            print ("|	 O")
            print ("|	\|/")
            print ("|	 |")
            print ("|")
            print ("|________")
        elif(failure==6):
            print ("_________")
            print ("|	 |")
            print ("|	 O")
            print ("|	\|/")
            print ("|	 |")
            print ("|	/ ")
            print ("|________")
        elif(failure ==7):
            print ("_________")
            print ("|	 |")
            print ("|	 O")
            print ("|	\|/")
            print ("|	 |")
            print ("|	/ \ ")
            print ("|________")
            print("You lose! The word was " + word_input)
            break

