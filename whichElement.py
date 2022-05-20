#!/usr/bin/python3

userChoice = 0
elements = ["air", "water", "fire", "earth"]
# make a list of questions 
# what's the logic, make a while loop that increments a counter to iterate through the project


def getUserInput():

    userInput = 0
    while userInput == 0:
       # global userInput 
       #herman suggests a try except for the error that I will 
        userInput = input("put in a number 1-4: ")
        if not userInput.isnumeric():
            print("that's not a number... use a number..")
            userInput = 0

        #create a function that will change it to a digit if it is one
        userInput = int(userInput)

        if userInput >= 5 or userInput == 0:
            print("that's not 1 through 4: ")
            userInput = 0

    return userInput

#we could have this number take in a parameter that then references the index on the list. 
def printQuestion1():
    print("choose a place to go \n kyoshi island \n Air Nomad Temple \n Ba Sing Se \n Spirit World ")
    return getUserInput()

def printQuestion2():
    print("choose your favorite phrase \n That's rough buddy \n MY CABBAGES \n There's no war in Ba Sing Se \n I don't need any Calming Tea")
    return getUserInput()

def printQuestion3():
    print(" choose a favorite familiar \n Lion Turtle \n Flying Bison \n Winged Lemur \n Elephant Koi")
    return getUserInput()

def printQuestion4():
    print(" choose a past life \n Kyoshi \n Roku \n Kuruk \n Yangchen")
    return getUserInput()

def printQuestion5():
    print(" choose a an item  \n Sokkas Boomerang \n Irohs Jasmine Tea \n  Aangs Staff \n Katara's necklace")
    return getUserInput()

def main():
    global userChoice
    #create a while loop, that while userChoice is < 5, we will loop through this. 
    userChoice += printQuestion1()
    #userChoice = getUserInput()
    print(userChoice)
    userChoice += printQuestion2()
    print(userChoice)
    userChoice += printQuestion3()
    print(userChoice)
    userChoice += printQuestion4()
    print(userChoice)
    userChoice += printQuestion5()
    
    print(userChoice)
    userChoice*=2
    elementDecider(userChoice)

def elementDecider(aNum):
    aNum= int(aNum)
    print(aNum)
    if aNum <= 10:
        print(elements[0])
    
    elif aNum < 10 and aNum <= 20:
        print(elements[1])
    
    elif aNum > 20 and aNum <= 30:
        print(elements[2])
    
    elif aNum > 30 and aNum <= 40:
        print(elements[3])
    else:
        print("idk how u fucked up and got away with it but here you are")

            
main()
