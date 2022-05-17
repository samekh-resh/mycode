#!/usr/bin/env python3

def main():
    userNum = int(input("what's a number you want to process? "))
    userNum2 = int(input("what's another number you want to process? "))
    x = 0 
    userCom = input("[a]dd, [s]ubtract, [m]ultipy, [d]ivide? ")
    
    def add(a, b):
        return a + b

    if(userCom == "a"):
        x = add(userNum, userNum2)
    elif(userCom =="s"):
        x = int(userNum) - int(userNum2)
    elif(userCom == "d"):
        x = int(userNum) / int(userNum2)
    elif(userCom == "m"):
        x = int(userNum) * int(userNum2)
    else:
        print("not a real command")
    print(x)

main()
