#Solicitar que o usuário digite as médias dos 4 bimestres
#fazer o cálculo da média geral.

#Classificar os alunos de acordo com a média geral.
#0,0 a 4,0 = muito ruim
#4,1 a 5,9 = ruim
#6,0 a 7,0 = regular
#7,1 a 8,0 = bom
#8,1 a 9,0 = muito bom
#9,1 a 10,0 = excelente

#Alem de classificar, verificar a situação:
#Regra 1: aprovado direto = media geral maior ou igual a 6,0
#Regra 2: em recuperacao = media geral menor do que 6,0 e maior do que 3,9
#Regra 3: reprovado direto = média geral abaixo de 4,0

print("Sistema de avaliação de alunos")
nota1 = float(input("Digite a média do 1o bimestre: "))
nota2 = float(input("Digite a média do 2o bimestre: "))
nota3 = float(input("Digite a média do 3o bimestre: "))
nota4 = float(input("Digite a média do 4o bimestre: "))

media = (nota1+nota2+nota3+nota4)/4

#Classificando os alunos
if media >=0 and media <= 4:
	print("\n>> Classificação: muito ruim")
elif media >=4.1 and media <= 5.9:
	print("\n>> Classificação: ruim")
elif media >=6.0 and media <= 7.0:
	print("\n>> Classificação: regular")
elif media >=7.1 and media <= 8.0:	
	print("\n>> Classificação: bom")
elif media >=8.1 and media <= 9.0:
	print("\n>> Classificação: muito bom")
elif media >=9.1 and media <= 10.0:
	print("\n>> Classificação: excelente")

#Verificando a situação
if media >= 6:
	print(">> Situação: aprovado direto")
elif media < 6 and media > 3.9:
	print(">> Situação: em recuperação")
else:
	print(">> Situação: reprovado direto")