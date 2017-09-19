#O usuario vai digitar a quantidade de horas trabalhadas, para que o programa calcule o valor do salario à receber.
#O programa deve ficar solicitando sempre novas quantidade de horas, até que seja digitado o valor 0 (zero)

#O calculo do salario bruto será a quantidade de horas * 20.5

def tela_inicial():
	print("Programa para calculcar salário líquido")
	horas_trabalhadas = float(input("Digite a quantidade de horas: "))
	return horas_trabalhadas

def calcular_salario_bruto(horas_trabalhadas):
	return horas_trabalhadas*20.5

def calcular_inss(salario_bruto):
	return salario_bruto*(11/100)

def calcular_fgts(salario_bruto):
	return salario_bruto*(8/100)

def calcular_leao(salario_bruto):
	return salario_bruto*(27.5/100)

def calcular_salario_liquido(salario_bruto, inss, fgts, leao):
	return salario_bruto-inss-fgts-leao

qtd_horas_trabalhadas = 0

while qtd_horas_trabalhadas >= 0 :
	qtd_horas_trabalhadas = tela_inicial()
	salario_bruto = calcular_salario_bruto(qtd_horas_trabalhadas)
	inss = calcular_inss(salario_bruto)
	fgts = calcular_fgts(salario_bruto)
	leao = calcular_leao(salario_bruto)
	salario_liquido = calcular_salario_liquido(salario_bruto, inss, fgts, leao)

	print("Salário bruto: ", salario_bruto)
	print("Salário líquido: ", salario_liquido)