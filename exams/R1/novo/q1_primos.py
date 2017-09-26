#Adicionar em uma lista, os números primos do intervalo de 0 a 100
#imprimir a lista ao final.

#Primo é todo numero que possui apenas dois divisores

#Um número X é divisor do número Y, quando o resto da divisão de
#Y por X é 0

lista_primos = []

for x in range(0, 101):
	cont = 0
	
	for y in range(1, x):
		if x%y==0:
			cont = cont+1
	if cont<2:
		lista_primos.append(x)

print(lista_primos)