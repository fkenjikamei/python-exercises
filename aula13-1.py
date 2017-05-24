# Solicite que digite as notas de todos
# os alunos da disciplina INPO, e calcule
# a media geral da turma 

somaNotas = 0

for x in range(1,5):
	print("Digite a nota do aluno ", x)
	nota = 0
	try:
		nota = float(input(""))
	except:
		print("Nota inválida!")

	somaNotas = somaNotas+nota

media = somaNotas/4

print("Media da turma: ",media)