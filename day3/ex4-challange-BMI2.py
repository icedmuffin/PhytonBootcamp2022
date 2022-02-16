# 🚨 Don't change the code below 👇
height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height = height/100
bmi_result = int(weight/height**2)

if bmi_result < 18.5:
    print(f"your body mass index is {bmi_result}, you are underweight.")
elif bmi_result < 25:
    print(f"your body mass index is {bmi_result}, you have a normal weight.")
elif bmi_result < 30:
    print(
        f"your body mass index is {bmi_result}, you are slightly overweight.")
elif bmi_result < 35:
    print(f"your body mass index is {bmi_result}, you are obese.")
else:
    print(f"your body mass index is {bmi_result}, you are clinically obese.")
