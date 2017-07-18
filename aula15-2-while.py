numero = 10
chances = 10

while(chances > 0):
	chute = int(input("Digite o chute: "))

	if(chute == numero):
		print("Acertou!")
		break

	if(chute > numero*2):
		chances -= 2
		print("Chute 2x maior! Menos duas chances")
	else:
		chances -= 1
		print("Menos uma chance")

