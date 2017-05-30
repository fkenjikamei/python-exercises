print("Loop ate 10, mas para se numero for negativo")

for x in range(1,11):
	print("Numero ", x)
	numero = int(input("Digite numero: "))

	if numero<0:
		print("Numero negativo!")
		break;
	else:
		print("Numero: ",numero)
		print("")