#Paginação utilizando o FOR
lista = [1, 0, 20, 3, 4, 5, 60, 7, 8, 9, 0]
qtd_itens_pagina = 2
tamanho = len(lista)

if(tamanho%2!=0):
	qtd_paginas = (tamanho//qtd_itens_pagina)+1
else:
	qtd_paginas = tamanho//qtd_itens_pagina

inicio = 0

for x in range(1, qtd_paginas+1):
	print("Página ",x)

	maximo = x*qtd_itens_pagina

	for y in range(inicio, len(lista)):
		if(y < maximo):
			print(lista[y])
		else:
			break

	inicio = x*qtd_itens_pagina