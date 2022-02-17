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
player1 = hand[int(input(
    "choose your hand \n 1.rock \n 2.paper \n 3. scissors \ntype the number :"))-1]

print(player1)

print("\n----VS----- \n")

player2 = hand[random.randint(0, 2)]
print(player2)

# logic
if player1 == rock:
    if player2 == paper:
        win = 0
    elif player2 == scissors:
        win = 1
    else:
        win = 2
elif player1 == paper:
    if player2 == scissors:
        win = 0
    elif player2 == rock:
        win = 1
    else:
        win = 2
elif player1 == scissors:
    if player2 == rock:
        win = 0
    elif player2 == paper:
        win = 1
    else:
        win = 2

if win == 1:
    print("yeay! you win!")
elif win == 0:
    print("you lose!")
else:
    print("draw!")
