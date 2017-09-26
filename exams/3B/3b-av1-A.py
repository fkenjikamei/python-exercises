#Campeonato de futebol
#vitoria = 3 pontos
#empate = 1 ponto
#derrota = 0 ponto

#Função que deve ser criada pontos_campeonato: recebe numero de vitórias, número de empates, e número de derrotas
#Função deve retornar se o time está classificado ou desclassificado

#Classificado >= 15 pontos, e desclassificado caso contrário

def pontos_campeonato(num_vitorias, num_empates, num_derrotas):
	total_pontos = (num_vitorias*3) + num_empates

	if total_pontos >= 15:
		return "Classificado"
	else:
		return "Desclassificado"

retorno = pontos_campeonato(2, 2, 0)
print(retorno)