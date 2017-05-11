#Inscricao no concurso da PM

ano_atual = 2017
ano_nascimento = int(input("Ano de nascimento? "))

idade = ano_atual-ano_nascimento

if idade > 18 :
	print("Pode se inscrever")
	print("Maior de idade")
else:
	print("Não pode se inscrever")