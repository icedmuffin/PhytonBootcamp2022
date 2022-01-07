# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# konversi data input

new_height = float(height)
new_weight = float(weight)

bmi_result = int(new_weight/new_height**2)

print("your body mass index is " + str(bmi_result))
