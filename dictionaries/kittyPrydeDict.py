#!/usr/bin/env python3
kitty = {"Real Name": "Katherine Anne Pryde",
        "Creators": ["Chris Claremont","John Byrne"],
        "Aliases" : ["Shadowcat", "Ariel", "Sprite", "Star-Lord (Star-Lady)", "Captain Kate Pryde", "Red Queen"],
        "Powers":"Phasing",
        "SAA": {"skills": "Ninja Training", "experience": ["Fighting Experience", " Leadership Experience"]}
        }


print(kitty["Creators"][0])

kitty["fave food"] = ["pistachios", "mac and cheese", "gravy.."]

print(kitty.keys())
print(kitty["fave food"][2])

#def choices():
    #choice = input("which key do you want to access? ")
    #return choice


#def main():
    #choice = choices()
    #if choice in kitty: 
    #    print(kitty[choice])
    #    print(f"kitty pryde's power is {kitty[choice]}")
    #else:    
    #    print("that wasn't an actual choice...")
    #    main()

#main()
