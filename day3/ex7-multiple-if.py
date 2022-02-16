
a = 7
if a > 7:
    print("bruh")
else:
    print("yooo")

print("------challange-------")
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? :"))
bill = 0

if height > 120:
    print("you can go")
    age = int(input("what's your age?"))
    if age < 12:
        print("the ticket is $5.00")
        bill = 5
    elif age <= 18:
        print("the ticket is $7.00")
        bill = 7
    else:
        print("the ticket is $12.00")
        bill = 12

    want_photo = input("you want a photo taken ? y or n : ")
    if want_photo == "y":
        bill += 3
        print("that would be $3.00, thanks!. ")

    print(f"your final bill is ${bill}.00")

else:
    print("you can not go")
