import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
hand = [rock, paper, scissors]


player1 = int(input(
    "choose your hand \n 0.rock \n 1.paper \n 2. scissors \ntype the number :"))

# filter start
if player1 >= 3:
    # lanjut
    player1_img = hand[player1]

    print(player1_img)

    print("\n----VS----- \n")

    # zona player2
    player2 = random.randint(0, 2)
    player2_img = hand[player2]
    print(player2_img)

    # logic
    win = 0
#    -----belum di buat

    if win == 1:
        print("yeay! you win!")
    elif win == 0:
        print("you lose!")
    else:
        print("draw!")

else:
    print("sorry, wrong input")
