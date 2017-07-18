#Paginação utilizando o FOR
import math

lista = [1, 0, 20, 3, 4, 5, 60, 7, 8, 9, 10, 11, 12, 20, 30, 40, 40, 20, 45, 29, 21]
qtd_itens_pagina = 5
qtd_paginas = math.ceil(len(lista)/float(qtd_itens_pagina))

print("Tamanho:",len(lista))

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