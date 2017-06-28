print("Adivinhação")
numeroSecreto = 79

chances = int(input("Quantos chutes? \n3-Tres chutes\n5-Cinco chutes\n8-Oito chutes "))

for x in range(1,chances+1):
	print("Chute de no.",x)
	chute = int(input("Qual o chute? "))

	if chute == numeroSecreto:
		print("Acertou!")
		break
	else:
		print("Errou!")