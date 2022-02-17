
from traceback import print_tb

print("--------------------")
prov_indonesia = ["jawa", "papua", "kalimantan", "maluku"]
print(prov_indonesia[0])
print("--------------------")
# alter list
prov_indonesia[0] = "jowo"
print(prov_indonesia)
print("--------------------")
# adding list
prov_indonesia.append("sumatera")
print(prov_indonesia)
print("--------------------")
# adding more list
prov_indonesia.extend(
    ["negara api", "kerajaan tahan", "suku air", "candi angin"])
print(prov_indonesia)

print("--------------------")
fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(dirty_dozen[1][1])
