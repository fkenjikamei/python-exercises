#Sistema para verificar velocidade dos carros

#abaixo de 60 = sem multa
#61 a 70 = 190,00
#71 a 80 = 260,00
#acima de 80 = 500,00

velocidade = float(input("Digite a velocidade: "))

if velocidade<=60:
	print("Sem multa!")
elif velocidade>=61 and velocidade<=70:
	print("Multa: 190,00")
elif velocidade>=71 and velocidade<=80:
	print("Multa: 260,00")
else:
	print("Multa: 500,00")
