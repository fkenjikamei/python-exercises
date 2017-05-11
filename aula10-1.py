#Jogo de Adivinhacao

numero_secreto = 32

print("*** Jogo de Adivinhacao ***\n\n")

chute = int(input("Digite um chute de 1 a 100: "))

if chute == numero_secreto :
	print("Acertou!")
elif chute > numero_secreto :
	print("Chute foi maior!")
else:
	print("Chute foi menor")








#if chute > numero_secreto :
#	print("Chute foi maior")

#if chute < numero_secreto :
#	print("Chute foi menor")

