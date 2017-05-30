#Um numero é primo se ele só possuir no máximo dois divisores

#O que é um divisor?
#R: quando dividimos um número por este, e o resto é ZERO

'''
4/4 = resto 0
4/3 = resto 1
4/2 = resto 0
4/1 = resto 0

12/12 = resto 0
12/11 = resto 1
12/10 = resto 2
12/9 = resto 3
12/8 = resto 4
12/7 = resto 5
12/6 = resto 0
12/5 = resto 7
12/4 = resto 0
12/3 = resto 0
12/2 = resto 0
12/1 = resto 0 *
'''

print("** Numero Primo **")

numero = int(input("Digite um numero: "))

cont = 0

for i in range(1, numero+1):
	if numero%i==0:
		cont = cont+1

print("Quantidade divisores: ",cont)

if cont<=2:
	print("Primo")
else:
	print("Nao primo")