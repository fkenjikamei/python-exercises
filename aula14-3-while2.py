numeroSecreto = 76
isAcertou = False
qtdChutes = 0

print("Adivinhação de 1 a 100")

while isAcertou == False:
	chute = int(input("Qual o chute? "))
	qtdChutes = qtdChutes + 1
	if chute == numeroSecreto:
		print("Acertou com ",qtdChutes," chute(s)")
		isAcertou = True
	else:
		print("Errou!")