isPrimo = False
cont = 0

while isPrimo == False:
	numero = int(input("Digite um número: "))
	
	for x in xrange(1,numero+1):
		if numero%x==0:
			cont = cont+1

	if cont <= 2:
		print("Primo!")
		break