print("** Jogo de Adivinhacao ** ")
print("\nNiveis do jogo:")
print("3 - Tres chances")
print("5 - Cinco chances")
print("8 - Oito chances")
chances = int(input("Escolha o nivel: "))

numeroSecreto = 83

for x in range(1, chances+1):
	chute = int(input("Digite um chute: "))

	if chute==numeroSecreto:
		print(">> Parabens! Acertou!")
		break
	elif chute>numeroSecreto:
		print(">> Chute foi maior")
	else:
		print(">> Chute foi menor")