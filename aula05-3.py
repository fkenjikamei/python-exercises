n_mat = float(input("Digite a nota em Matematica: "))
n_ingles = float(input("Digite a nota em ingles: "))
n_port = float(input("Digite a nota em Portugues: "))
n_inpo = float(input("Digite a nota em Int. Progracao: "))

peso_mat = 3
peso_ingles = 2
peso_port = 1
peso_inpo = 5

soma_pesos = peso_mat+peso_ingles+peso_port+peso_inpo
media_ponderada = ((n_mat*peso_mat) + (n_ingles*peso_ingles) + (n_port*peso_port) + (n_inpo*peso_inpo))/soma_pesos

print("Media ponderada = ",media_ponderada)