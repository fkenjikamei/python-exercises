#Questão 3
#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F -
#Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite o sexo (f-feminino e m-masculino): ")

if sexo=='m' or sexo=='M':
	print("Masculino")
elif sexo=='f' or sexo=='F':
	print("Feminino")
else:
	print("Sexo inválido")