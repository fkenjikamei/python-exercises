#Operadores matematicos

operador = input("Qual operação deseja realizar? (+ - / *) :")

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))

if operador == '+':
	print("Soma = ", (num1+num2))
elif operador == '-':
	print("Subtração = ", (num1-num2))
elif operador == '*':
	print("Multiplicação = ", (num1*num2))
elif operador == '/':
	print("Divisão = ", (num1/num2))
else:
	print("Operação invalida!")

# StackOverflow