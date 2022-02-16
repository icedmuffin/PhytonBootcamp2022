import turtle


name1 = input("what is your name?").lower()
name2 = input("what is her/his name?").lower()
merge_name = name1 + name2

print(merge_name)
# cont true letters
t_count = merge_name.count("t")
r_count = merge_name.count("r")
u_count = merge_name.count("u")
e_count = merge_name.count("e")

true_total = int(t_count+r_count+u_count+u_count+e_count)
print(true_total)

# count love letters
l_count = merge_name.count("l")
o_count = merge_name.count("o")
v_count = merge_name.count("v")
e_count = merge_name.count("e")

love_total = int(l_count+o_count+v_count+e_count)
print(love_total)

result = int(str(true_total)+str(love_total))
print(result)

if (result < 10) or (result > 90):
    print(
        f"you guys score are {result}%, you go together like coke and mentos!")
elif (result >= 40) and (result <= 50):
    print(
        f"you guys score are {result}%, you are alright together")
else:
    print(
        f"you guys score are {result}%, too bad")
