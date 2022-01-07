# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
new_age = int(age)
remain_years = 70 - new_age
remain_months = 12*remain_years
remain_weeks = 52*remain_years
remain_days = 365*remain_years

print(
    f"you have {remain_days} days, {remain_weeks} weeks, {remain_months} months, {remain_years} years left.")
