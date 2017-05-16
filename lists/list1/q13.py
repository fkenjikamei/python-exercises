
sexo = raw_input("Digite o sexo: ")
altura = float(input("Qual a altura: "))

if sexo == "m" :
	peso_ideal = (72.7 * altura)-58
else :
	peso_ideal = (62.1 * altura)-44.7

peso = float(input("Digite o peso: "))

if peso > peso_ideal :
	print "Acima do peso ideal"
else :
	print "Abaixo do peso ideal"