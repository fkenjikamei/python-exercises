lista_numeros = []
lista_chutes = []
lista_acertos=[]
valida_nivel = False
ganhou = False

while len(lista_numeros) < 5:
	numero = int(input("Digite um numero positivo menor que 100: "))

	if numero > 0 and numero < 100:
		if numero in lista_numeros:
			print("Número já foi digitado antes")
		else:
			lista_numeros.append(numero)
	else:
		print("Número deve ser de 1 a 99")

while valida_nivel == False:
	print("Nivel: ")
	print("1- Oito chances")
	print("2- Dez chances")
	print("3- Doze chances")
	nivel = int(input("Qual o nivel escolhe: "))

	valida_nivel = True

	if nivel==1:
		chances = 8
	elif nivel == 2:
		chances == 10
	elif nivel == 3:
		chances = 12
	else:
		print("Nivel invalido!")
		valida_nivel = False

while chances > 0:
	if len(lista_numeros)==len(lista_acertos):
		ganhou = True
		break

	chute = int(input("Qual o seu chute? "))

	if chute in lista_numeros:
		if chute in lista_chutes:
			print("Você já chutou esse número.")
		else:
			lista_chutes.append(chute)
			lista_acertos.append(chute)
			print("Acertou!")
			chances -= 1
	else:
		print("Você errou!")
		lista_chutes.append(chute)
		chances -= 1


if ganhou == True:
	print("Parabéns! Você ganhou")
else:
	print("Infelizmente perdeu! Tente novamente.")


print("Quantidade de acertos: ", len(lista_acertos))
print("Numeros acertados: ", lista_acertos)