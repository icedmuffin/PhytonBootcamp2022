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

print(player1)
# filter start
if player1 <= 3 or player1 > 0:
    # lanjut
    player1_img = hand[player1]

    print(player1_img)

    print("\n----VS----- \n")

    # zona player2
    player2 = random.randint(0, 2)
    player2_img = hand[player2]
    print(f"player 2 {player2}")
    print(player2_img)

    # logic
    win = 0
    if player1 == 0 and player2 == 2:
        win = 1
    elif player2 == 0 and player1 == 2:
        win = 0
    elif player1 < player2:
        win = 1
    elif player2 < player1:
        win = 0
    elif player1 == player2:
        win = 3

    if win == 1:
        print("yeay! you win!")
    elif win == 0:
        print("you lose!")
    else:
        print("draw!")

else:
    print("sorry, wrong input")
