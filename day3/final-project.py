# link flowchart
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


from glob import escape


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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("-------------------")

answer1 = input("you entering a huge garden labrinth and stuck at a plit way, right and left. \n suddenly there are a mist coming from no where. \n you saw ur ex in the right, and a chest full of gold on the left. \n which way do you choose? right (r) or left (l)?").lower()
if answer1 == "l":
    print("-------------------")
    answer2 = input("you manage to get trough the mist, you meet a river,\n there are a monkey swing on the river, do you wait for the monkey to leave or swim by?\n swim (a) or wait (b) ?").lower()
    if answer2 == "b":
        print("-------------------")
        answer3 = input(
            "on the end of the road you saw 3 door with different color, \n which color do you choose ? red (a), blue(b), yellow(c)?").lower()
        if answer3 == "c":
            print("-------------------")
            print("you enter the room, and finally found the gold chess!\n you are rich")
        elif answer3 == "b":
            print("-------------------")
            print(
                "when you enter blue door you fall into deep ocean.\n you died")
        elif answer3 == "a":
            print("-------------------")
            print(
                "when you enter red door you fall into a place full of fire. \n you are dead.")
    else:
        print("-------------------")
        print("monkey get offended and start grabing your foot,\n you start to drowning, you are dead.")
else:
    print("-------------------")
    print("ex is always the wrong answer, she stab you, you are dead.")
