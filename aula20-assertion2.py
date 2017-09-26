#Criar uma funcao que verifica se o aluno está ou não em recuperação

def verifica_situacao_aluno_recuperacao(media1, media2, media3, media4):
	media = (media1+media2+media3+media4)/4
	if media >= 6.0:
		return "Aprovado"
	else:
		return "Em recuperacao"

assert("Aprovado" != verifica_situacao_aluno_recuperacao(10.0, 5.0, 10.0, 7.0))