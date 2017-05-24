
#Escopo de variáveis

nota = float(input("Digite a nota: "))

if nota < 6:
	valor = input("Fez recuperação? ")
	print("Nota: ", nota)

	for x in range(1,3):
		print("Valor: ", valor)
		print("Nota: ", nota)

print(valor)