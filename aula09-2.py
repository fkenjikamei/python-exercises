#Sistema para realizar inscrição em um evento
#Regra: Identificar a categoria da pessoa com base 
#		na idade

ano_atual = 2017
ano_nascimento = int(input("Ano de nascimento? "))

idade = ano_atual-ano_nascimento

if idade==0 :
	print("Bebê")

elif idade>0 and idade<=10 :
	print("Criança")

elif idade>10 and idade<=17 :
	print("Adolescente")

elif idade>17 and idade<60 :
	print("Adulto")

else:
	print("Idoso")