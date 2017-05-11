#Tabela Verdade

print("Tabela Verdade - AND\n")

num1 = 10
num2 = 20
num3 = 30
num4 = 40

print(num1 < num2 and num3 < num4)
print(num3 < num4 and num1 > num2)
print(num1 > num2 and num3 < num4)
print(num4 < num1 and num2 > num4)

print("")

print("Tabela Verdade - OR\n")
print(num1 <= num2 or num3 != num4)
print(num4 >= num1 or num2 == num3)
print(num2 > num3 or num4 != num3)
print(not(num1<num4) or num2 > num3)