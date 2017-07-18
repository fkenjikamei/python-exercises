'''
A partir do código do programa anterior, 
modifique-o para que ele exiba um quadrado vazio. 
Por exemplo, se seu programa ler um tamanho 5, 
ele deverá exibir:
****
*  *
*  *
****
'''

tamanho = int(input("Digite o tamanho (inteiro): "))

for x in range(1,tamanho):
	if x == 1 or x == tamanho-1:
		for y in range(1, tamanho-1):
			print("*",end='')
		print("*")
	else:
		print("*")