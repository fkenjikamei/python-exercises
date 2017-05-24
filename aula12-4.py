print("Operações Matemáticas entre dois números")

try:
	num1 = int(input("Digite o primeiro número: "))
	num2 = int(input("Digite o segundo número: "))

	print("Soma: ",num1+num2)
	print("Subtração: ",num1-num2)
	print("Multiplicação: ",num1*num2)
	print("Divisão: ",num1/num2)
except:
	print("Erro!")

print("Sai...")