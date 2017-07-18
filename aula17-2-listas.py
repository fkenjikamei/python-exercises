#Lista - Adicionando e removendo valores

nomes = ["Fulano","Ciclano"]
print(nomes)
nomes.append("Beltrano")
print(nomes)

nomes = ["Beltrano"] + nomes
print(nomes)

nome_remover = input("Nome a remover? ")

for x in range(0, len(nomes)):
	if(nome_remover in nomes):
		nomes.remove(nome_remover)

	if(nome_remover not in nomes):
		break

print(nomes)