import random

#we're making a random number game
#generates random number between 1-100
#five guesses to get the answer right, guess too high, it should say too high, same for too low. 
#if logic, while logic, 

answer = random.randint(1, 100)
guess = ""
guesses = 0
while guesses < 5 and guess != answer:
    try:
        guess = int(input("guess a number between 1 and 100 " )) 
    
        guesses += 1

        if guess < answer:
            print("too low")
    
        elif guess > answer:
            print("too high")
    
        else:
            print("it's correct")
    
    except:
        print("not a valid number")
    
