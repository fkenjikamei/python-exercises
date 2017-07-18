lista_notas = [5.0, 3.0, 4.5]

print("Lista")

print("Tamanho: ",len(lista_notas))

for x in range(0, len(lista_notas)):
	print("Posicao: [",x,"] = ",lista_notas[x])

lista_misturada = [9.5,lista_notas]
print(lista_misturada[1][1])