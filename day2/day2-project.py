# final project day 2
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("--------tip calculator------")
total = float(input("what was the total bill? $"))
tip = float(input("how much is your tip in percentage ?"))
ind = int(input("how many person you wanna split the bill? "))
ind_bill = round((total*(1 + (tip/100)))/ind, 2)

# ini special function - format, belum dipelajar, intinya ingin ada 2 angka di belakang koma
final_bill = "{:.2f}".format(ind_bill)

print(f"each person should pay : ${final_bill}")

"----or-----"
print(f"each person should pay : $ {ind_bill:.2f}")
