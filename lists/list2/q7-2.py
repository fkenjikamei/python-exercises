#Questão 7
#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1>num2>num3:
	maior=num1
	menor=num3

if num1>num3>num2
	maior=num1
	menor=num2

if num2>num1>num3:
	maior=num2
	menor=num3

if num2>num3>num1
	maior=num2
	menor=num1

if num3>num1>num2:
	maior=num3
	menor=num1

if num3>num2>num1
	maior=num3
	menor=num1

print("Maior: ",maior)
print("Menor: ",menor)