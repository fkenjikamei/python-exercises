#Solicite ao usuário 5 números
#os números devem ser maior que 0 e menores que 100
#armazene os numeros em uma lista

numeros = []
chances = 0
chutes = []
acertos = []

while len(numeros) < 5:
	numero = int(input("Digite um numero positivo menor que 100: "))

	if numero in numeros:
		print(">> Número já adicionado")
	elif numero>=0 and numero<100:
		numeros.append(numero)
		print(">> Número adicionado com sucesso")
	else:
		print(">> Número fora do intervalo")

print("\n\n** O jogo já vai começar.. **")


while chances == 0:
	nivel = int(input("Qual o nivel que deseja? \n1- 8 chances \n2- 10 chances \n3- 12 chances\n"))

	if nivel == 1:
		chances = 8
	elif nivel == 2:
		chances = 10
	elif nivel == 3:
		chances = 12
	else:
		print(">> Escolha um nível válido")

while chances > 0:
	if len(acertos) == len(numeros):
		print("Você ganhou! Parabéns!")
		break

	print(">> Você tem ",chances," chances")
	chute = int(input("Qual o seu chute? "))
	chutes.append(chute)

	if chute in acertos:
		print(">> Número já foi acertado antes!")
		chances = chances+1
	elif chute in numeros:
		print(">> Acertou")
		acertos.append(chute)
	else:
		print("Errou!")

	chances = chances-1

print("** Placar final **")
print("Chutes: ",chutes)
print("Acertos: ",acertos)
