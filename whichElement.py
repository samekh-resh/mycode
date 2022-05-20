#!/usr/bin/python3

userChoice = 0
elements = ["air", "water", "fire", "earth"]

def getUserInput():
    userInput = 0
    while userInput == 0:
       # global userInput 
        userInput = int( input("put in a number 1-4: "))
        #create a function that will change it to a digit if it is one

        if userInput >= 5:
            print("that's not 1 through 4: ")
            userInput = 0

    return userInput

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
