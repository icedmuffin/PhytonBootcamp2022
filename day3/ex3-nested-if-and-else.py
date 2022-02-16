

a = 7
if a > 7:
    print("bruh")
else:
    print("yooo")

print("------challange-------")
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("you can go")
    age = int(input("what's your age?"))
    if age < 12:
        print("the ticket is $5.00")
    elif age <= 18:
        print("the ticket is $7.00")
    else:
        print("the ticket is $12.00")
else:
    print("you can not go")
