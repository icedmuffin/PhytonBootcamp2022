import random

# input data
names_string = input("Give me everybody's names, separated by a comma. ")

# spiting data ke dalam list
names = names_string.split(", ")

print(names)

# random list
should_pay = names[random.randint(0, len(names)-1)]
print(f"the one who will pay the food this night is {should_pay}")

print("\n \n \n ----------------------------")

# alternative random list
random_person = random.choice(names)
print(f"the one who will pay the food this night is {random_person}")
