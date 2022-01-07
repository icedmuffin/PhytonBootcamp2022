print("------pembulatan angka-------")
print(round(8/3))
print("------pembulatan angka presisi 2 angka dibelakang koma-------")
print(round(8/3, 2))

print("------floor division--------")
print("megambil angka depan tampa koma, hasilnya adalah tipe data integer")
print(8//3)

print("------operasi secara terus menerus--------")
result = 4/2
print(result)

result /= 2
print(result)

print("------operasi secara terus menerus 2 --------")
result += 1
print(result)
result += 1
print(result)

print("------f String --------")
print("digunakan untuk measukan berbagai jenis tipe data ke string tanpa harus di konversi.")
print("like this :")
score = 98
height = 1.67
isWinning = True
print(
    f"your score is {score}, your height is {height}. you are winning status is {isWinning}")
