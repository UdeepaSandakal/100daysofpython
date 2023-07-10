print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************

'''
      )
print("\nWelcome to treasure island\nYour mission is find the hidden treasure.")
choice01 = input('\nYou\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice01 == "left":
    choice02 = input(
        '\nYou \'re come to a lake.There is an island in the middle of the lake. \nType "wait" to wait for a boat. '
        'Type '
        '"swim" to swim across. ').lower()
    if choice02 == "wait":
        choice03 = input('\nYou arrive at the island unharmed. There is a house with 3 doors.\nOne red,one yellow and one blue. hich color do you choose ').lower()
        if choice03 == "red":
            print("\nIt's a room full of fire. Game Over.")
        elif choice03 == "yellow":
            print("\nYou found the treasure! You win!")
        elif choice03 == "blue":
            print("\nYou enter a room of beats. Game Over.")
        else:
            print("\nYou choose a door that doesn't exist. Game Over.")
    else:
        print("\nYou got attacked by an angry trout. Game Over.")


else:
    print("\nYou fell into a hole. Game over.")
