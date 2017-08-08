print("Adivinhacao")
chutes=[]
numeroSecreto = 10

acertou=False

#Enquanto uma condição for Verdadeira!
while acertou==False:
	chute = int(input("Qual o chute?"))
	chutes.append(chute)

	if chute == numeroSecreto:
		print("Acertou!")
		acertou=True

print("Seus chutes foram: ")
for x in range(0, len(chutes)):
	print(chutes[x])