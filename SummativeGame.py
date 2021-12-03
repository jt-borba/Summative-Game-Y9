import random
import termcolor
import playsound
import art
import textgamelib

inventory = []
finalInventory = ["Rope", "Cloth", "Clip", "Plane", "Pro Skydiver"]
direction = ("")
word=art.text2art("Welcome to" "\nJebari Adventures")
print (word)

name = input("The game will now begin please start by inputing your name:")
name += ":"
print("Welcome", name,)

tutorial = "In this game you will help Jebari out with various tasks. These tasks include getting materials, helpers and building things. \nThis is a tutorial on how to play. To go North type north, to go east type east, to go south type south, to go west type west. \nIf you at any point need this tutorial again, instead of scrolling back up just type help. \nThe game must be played through the terminal don't try to access the code in any way. \nTo complete the game you must collect the following items: Rope, Cloth, Clip, Plane, Pro Skydiver"
print(tutorial)

print("\n", name, "Hmm I wonder where Jebari is? Maybe I should look for him. You go North towards the Grand Canyon.")
print("You arrive at the Grand Canyon to see Jebari looking sad.")
print(name, "What's wrong?")
print("Jebari: I want to go parachuting but I don't know how to get the things I need. Could you help me?")
print(name, "Sure!")
print ("Jebari: I need cloth, string and a plane. Oh and also if you could get an instructor that would be great.")

print("Please go south towards the city")

positionRow = 0
positionColumn = 3

correct = False
while not correct:
    answer2 = input("What direction do you want to go?")
    if 'east' in answer2.lower():
        correct = False
    if 'west' in answer2.lower():
        correct = False
    if 'north' in answer2.lower():
        correct = False
    if 'south' in answer2.lower():
        correct = True
        positionRow += 1
    else:
        print("Please go south ")

print("Welcome to Pheonix, Arizona. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop.")

while set(finalInventory) != set(inventory):
    direction = input("Enter your command: ").lower()
    if "south" in direction:
        positionRow += 1
    if "north" in direction:
        positionRow -= 1
    if "west" in direction:
        positionColumn -= 1
    if "east" in direction:
        positionColumn += 1
    if "help" in direction:
        print(tutorial)
    if "inventory" in direction:
        print(textgamelib.printObjectList(inventory))
    if positionRow == 1 and positionColumn == 2:
        clothShop = input("Welcome to the cloth shop. You can buy: Cloth ")
        clothShop = clothShop.lower()
        if "Cloth" in inventory and "cloth" in clothShop:
            print("You already have that. To exit the shop go East. ")
        else:
            if "cloth" in clothShop and "cloth" not in inventory:
                inventory.append("Cloth")
                print("Cloth has been added to your inventory. To exit the shop go east. ")
    if positionRow == 2 and positionColumn == 2:
        skydivershangoutinventory = input("Welcome to the skydivers hangout, what do you need? Here you can hire an Instructor. ")
        skydivershangoutinventory = skydivershangoutinventory.lower()
        if "Pro Skydiver" in inventory and "instructor" in skydivershangoutinventory:
            print("You already have that. To exit go east. ")
        else:
            if "instructor" in skydivershangoutinventory and "Pro Skydiver" not in inventory:
                inventory.append("Pro Skydiver")
                print ("Private instructor added to your inventory. To exit go east. ")
    if positionRow == 3 and positionColumn == 3:
        house = input("Welcome to the Realtor what would you like to do?: Buy a house? ")
        house = house.lower()
        if "House" in inventory and "house" in house:
            print("You already have that. To exit go North. ")
        else:
            if "house" in house and "House" not in inventory:
                inventory.append("House")
                print("Thank you for buying, you may now enter the house. To exit the realtor go north. ")
    if positionRow == 0 and positionColumn == 3:
        print("Welcome to the Grand Canyon to enter the city go south. ")
    if positionRow == 1 and positionColumn == 3:
        print("Welcome to Pheonix Arizona. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop.")
    if positionRow == 2 and positionColumn == 3:
        print("To the North there is an intersection. To the south there is a realtor. To the west there is a Skydivers Hangout. To the east there is a rockclimbing shop. ")
    if positionRow == 0 and positionColumn == 4 and "House" not in inventory:
        print("The house is locked if you would like to buy it go to the Realtor. You have been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
        positionRow = 1
        positionColumn = 3
    if positionRow == 0 and positionColumn == 4 and "House" in inventory:
        print("Welcome to your house. To leave go south. ")
    if positionRow == 1 and positionColumn == 4:
        print("To the north there is a house. To the east there is a private airport. To the south there is a rockclimbing shop. To the west there is an intersection. ")
    if positionRow == 2 and positionColumn == 4:
        rockClimbingShop = input("Welcome to the Rockclimbing shop. You can buy: Rope, Clip. ")
        rockClimbingShop = rockClimbingShop.lower()
        if "Rope" in inventory and "rope" in rockClimbingShop:
            print("You already have that. To exit go west. ")
        else:
            if "rope" in rockClimbingShop and "Rope" not in inventory:
                inventory.append("Rope")
                print("Thanks for buying! Rope has been added to your inventory. To exit go west. ")
        if "Clip" in inventory and "clip" in rockClimbingShop:
            print("You already have that. To exit go west. ")
        else:
            if "clip" in rockClimbingShop and "Clip" not in inventory:
                inventory.append("Clip")
                print("Thanks for buying! Clip has been added to your inventory. To exit go west. ")
    if positionRow == 1 and positionColumn == 5:
        privateAirport = input("Welcome to the private airport. What do you need? Here you can get a plane with a pilot. ")
        privateAirport = privateAirport.lower()
        if "Plane" in inventory and "plane" in privateAirport:
            print("You alredy have that. To exit go west. ")
        else:
            if "plane" in privateAirport and "Plane" not in inventory:
                inventory.append("Plane")
                print("Your plane will arrive with a pilot. To exit go west. ")
    if positionRow == 0 and positionColumn == 2:
        positionColumn = 3
        positionRow = 1
        print ("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 1 and positionColumn == 1:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 2 and positionColumn == 1:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 3 and positionColumn == 2:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 4 and positionColumn == 3:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 3 and positionColumn == 4:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ") 
    if positionRow == 2 and positionColumn == 5:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 1 and positionColumn == 6:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 0 and positionColumn == 5:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")

print ("You have completed the game, thank you for playing! Your current inventory is:", inventory)
continueornot = input("If you would like to continue going around the city, enter 'continue'. If not enter 'stop'")
continueornot = continueornot.lower()
while "stop" not in continueornot and "stop" not in direction:
    if "continue" in continueornot or "south" in continueornot or "north" in continueornot or "west" in continueornot or "east" in continueornot:
        direction = input("Enter your command: ").lower()
    if "south" in direction:
        positionRow += 1
    if "north" in direction:
        positionRow -= 1
    if "west" in direction:
        positionColumn -= 1
    if "east" in direction:
        positionColumn += 1
    if "help" in direction:
        print(tutorial)
    if "inventory" in direction:
        print(textgamelib.printObjectList(inventory))
    if positionRow == 1 and positionColumn == 2:
        clothShop = input("Welcome to the cloth shop. You can buy: Cloth ")
        clothShop = clothShop.lower()
        if "Cloth" in inventory and "cloth" in clothShop:
            print("You already have that. To exit the shop go East. ")
        else:
            if "cloth" in clothShop and "cloth" not in inventory:
                inventory.append("Cloth")
                print("Cloth has been added to your inventory. To exit the shop go east. ")
    if positionRow == 2 and positionColumn == 2:
        skydivershangoutinventory = input("Welcome to the skydivers hangout, what do you need? Here you can hire an Instructor. ")
        skydivershangoutinventory = skydivershangoutinventory.lower()
        if "Pro Skydiver" in inventory and "instructor" in skydivershangoutinventory:
            print("You already have that. To exit go east. ")
        else:
            if "instructor" in skydivershangoutinventory and "Pro Skydiver" not in inventory:
                inventory.append("Pro Skydiver")
                print ("Private instructor added to your inventory. To exit go east. ")
    if positionRow == 3 and positionColumn == 3:
        house = input("Welcome to the Realtor what would you like to do?: Buy a house? ")
        house = house.lower()
        if "House" in inventory and "house" in house:
            print("You already have that. To exit go North. ")
        else:
            if "house" in house and "House" not in inventory:
                inventory.append("House")
                print("Thank you for buying, you may now enter the house. To exit the realtor go north. ")
    if positionRow == 0 and positionColumn == 3:
        print("Welcome to the Grand Canyon to enter the city go south. ")
    if positionRow == 1 and positionColumn == 3:
        print("Welcome to Pheonix Arizona. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop.")
    if positionRow == 2 and positionColumn == 3:
        print("To the North there is an intersection. To the south there is a realtor. To the west there is a Skydivers Hangout. To the east there is a rockclimbing shop. ")
    if positionRow == 0 and positionColumn == 4 and "House" not in inventory:
        print("The house is locked if you would like to buy it go to the Realtor. You have been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
        positionRow = 1
        positionColumn = 3
    if positionRow == 0 and positionColumn == 4 and "House" in inventory:
        print("Welcome to your house. To leave go south. ")
    if positionRow == 1 and positionColumn == 4:
        print("To the north there is a house. To the east there is a private airport. To the south there is a rockclimbing shop. To the west there is an intersection. ")
    if positionRow == 2 and positionColumn == 4:
        rockClimbingShop = input("Welcome to the Rockclimbing shop. You can buy: Rope, Clip. ")
        rockClimbingShop = rockClimbingShop.lower()
        if "Rope" in inventory and "rope" in rockClimbingShop:
            print("You already have that. To exit go west. ")
        else:
            if "rope" in rockClimbingShop and "Rope" not in inventory:
                inventory.append("Rope")
                print("Thanks for buying! Rope has been added to your inventory. To exit go west. ")
        if "Clip" in inventory and "clip" in rockClimbingShop:
            print("You already have that. To exit go west. ")
        else:
            if "clip" in rockClimbingShop and "Clip" not in inventory:
                inventory.append("Clip")
                print("Thanks for buying! Clip has been added to your inventory. To exit go west. ")
    if positionRow == 1 and positionColumn == 5:
        privateAirport = input("Welcome to the private airport. What do you need? Here you can get a plane with a pilot. ")
        privateAirport = privateAirport.lower()
        if "Plane" in inventory and "plane" in privateAirport:
            print("You alredy have that. To exit go west. ")
        else:
            if "plane" in privateAirport and "Plane" not in inventory:
                inventory.append("Plane")
                print("Your plane will arrive with a pilot. To exit go west. ")
    if positionRow == 0 and positionColumn == 2:
        positionColumn = 3
        positionRow = 1
        print ("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 1 and positionColumn == 1:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 2 and positionColumn == 1:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 3 and positionColumn == 2:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 4 and positionColumn == 3:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 3 and positionColumn == 4:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ") 
    if positionRow == 2 and positionColumn == 5:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 1 and positionColumn == 6:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")
    if positionRow == 0 and positionColumn == 5:
        positionColumn = 3
        positionRow = 1
        print("You can't go there. You've been returned to the city square. To North there is the Grand Canyon. To the South there is a road. To the East there is a road. To the West there is a cloth shop. ")

if "stop" in continueornot:
    print("Okay thank you playing. The game will now exit.")