#Questão 7
#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = 0
menor = 0

if num1>num2 and num1>num3:
	maior=num1
	if num2<num3:
		menor=num2
	else:
		menor=num3
elif num2>num1 and num2>num3:
	maior=num2
	if num1<num3:
		menor=num1
	else:
		menor=num3
elif num3>num1 and num3>num2:
	maior=num3
	if num1<num2:
		menor=num1
	else:
		menor=num2

print("Maior: ",maior)
print("Menor: ",menor)