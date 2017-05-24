#Fazer um programa que solicite 5 números
#e informe se o número é par ou impar

for x in range(1,6):
	numero = int(input("Digite um número: "))
	if numero%2==0 :
		print(numero," é um número par")
	else:
		print(numero," é um número ímpar")