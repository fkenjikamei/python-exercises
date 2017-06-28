isPrimo = False

while isPrimo == False:
	cont = 0
	numero = int(input("Digite um número: "))
	
	for x in range(1,numero+1):
		if numero%x==0:
			cont = cont+1

	if cont == 2:
		print("Primo!")
		isPrimo = True