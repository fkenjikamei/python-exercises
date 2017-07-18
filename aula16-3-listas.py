numeros = [10, 20, 30, 10]

numero = int(input("Digite um numero: "))
ocorrencias = 0

print("\nUtilizando o FOR")
for x in range(0, len(numeros)):
	if(numero == numeros[x]):
		ocorrencias +=1

print("Ocorrencias: ",ocorrencias)


print("\n\nUtilizando o WHILE")

tamanho = len(numeros)

while(tamanho > 0):
	print(numeros[tamanho])
	tamanho -= 1	
