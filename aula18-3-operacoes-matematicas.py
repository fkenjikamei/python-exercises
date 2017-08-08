def mensagemBoasVindas():
	print("Minha primeira calculadora")
	nome = input("Qual o seu nome? ")
	print("Seja bem vindo ", nome)

def somar(numero1, numero2):
	print("Soma: ",numero1+numero2)

def subtrair(numero1, numero2):
	print("Resultado da Subtracao: ", numero1-numero2)

def multiplicar(numero1, numero2):
	print("Multiplicar: ", numero1*numero2)

def dividir(numero1, numero2):
	print("Dividir: ", numero1/numero2)


mensagemBoasVindas()
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
somar(num1, num2)
subtrair(num1, num2)
multiplicar(num1, num2)
dividir(num1, num2)

print("Qualquer coisa...")
num3 = int(input("Numero 3: "))
num4 = int(input("Numero 4: "))
somar(num3, num4)
subtrair(num3, num4)
multiplicar(num3, num4)
dividir(num3, num4)