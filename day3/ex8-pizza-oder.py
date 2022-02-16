print("welcome to pizza hot delivery")
pizza_size = input("what ur pizza size? s, m or l ?")
toping_pep = input("do you want pepperoni toping? y or n?")
toping_che = input("do you want cheese toping? y or n?")

bill = 0
if pizza_size == "s":
    bill = 15
    if toping_pep == "t":
        bill += 2
elif pizza_size == "m":
    bill = 20
    if toping_pep == "y":
        bill += 3
elif pizza_size == "l":
    bill = 25
    if toping_pep == "y":
        bill += 3

if toping_che == "y":
    bill += 1

print(f"your final bill would be ${bill}.00")
