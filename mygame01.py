#!/usr/bin/python3
# to dos] description of each room and each item and display that 
#will need a dictionary for each, string of the key and value with a string of the description
room_description ={
        'Hall' : {'description': 'a long dimly lit hallway with doors that lead [up] the Attic, [south] to the Kitchen, [east] to the Dining Room'},
        'Kitchen': {'description': 'a large open room full of dilapidated cabinets, and a strong, stench resembling that of a rotten milk. From Kitchen you can go [down] to get to the Basement or [north] to return to the Hall'},
        'Dining Room':{'description': 'A once beautiful room with a grand table and ornate woodwork, covered in fine silver, now covered in cobwebs. You may go [west] to the Hall, [south] to the Garden, and [north] to the Pantry'},
        'Garden' :{'description': 'An overgrown garden with an odd glow coming from somewhere just out of sight. Head [north] to go to the Dining Room.'},
        'Pantry':{'description':'A large butler\'s pantry that appears to be untouched still having some food inside. From the Pantry you can head [south] to the Dining Room.'},
        'Attic' : {'description': 'a hot dark space only pieces of it can be seen by sunlight peeking through holes from the attic turbines. Who knows what could exist up here.'},
        'Basement' : {'description': 'a large open space that was used as a livingroom. Go [up] to return to the kitchen.'}
        }

riddle_Dictionary = {
        'key': "To open a door you can knock or use this item to unlock",
        'cookie': 'I’m round but I’m not a wheel I’m loved by a monster but I’m not the Bride of Frankenstein I sometimes contain chips but I’m not a computer I go well with milk but I’m not a bowl of cereal I’m made of dough but I’m not a loaf of bread',
        'potion': 'drink booze you feel bad, drink me, you feel good. witches raised me.'
        }
#when user chooses get item they must answer a riddle from the riddle bank
def riddleFunction():
    answer= input(">")
    if move[0] == 'get'
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            solveTheRiddle(answer)

def solveTheRiddle(answer):
    if answer in riddle_dictionary.keys():
        print('correct')
        inventory += [answer]
        #display a helpful message
        print(answer + ' got!')
        #delete the item from the room
        del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
    #tell them they can't get it
    print('Can\'t get ' + answer + '!')


# Replace RPG starter project with this code when new instructions are live
#def solveTheRiddle(aWord):
#    if aword in riddleList:
#        print(riddleList[aWord])
#        playerAnswer = input("what is your solution to this riddle? ")
#        if playerAnswer == riddleList[aword][1]:
#            return True
#        else:
#            print("sorry... wrong submit.")
#            return False
                


def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom + '. ' + room_description[currentRoom]['description'])
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'


showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)
    
  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #this is where we would add the logic for the riddle. 
      riddleFunction()
      #didTheyPassRiddle(rooms[currentRoom]['item']) 
      #add the item to their inventory
      wasItSolved = solveTheRiddle()
      
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    if 'cookie' in inventory:
        print('you were benevolent and gave the monster your cookie...YOU WIN')
        break
    #if else logic here, that if the cookie is in your inventory, then  it will say you gave the monster the cookie and you won! 
    print('A monster has got you... GAME OVER!')
    break
