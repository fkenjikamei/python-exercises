import os

valorIngresso=0
listaDevedores=[11111111111,22222222222]
listaCompradores=[]
valorVendas=0
cpf=0

def limparTela():
	os.system('cls' if os.name == 'nt' else 'clear')


def definirValor():
	limparTela()
	global valorIngresso
	validarValor = False
	
	while validarValor == False:
		try:
			valorIngresso = float(input("Qual o valor do ingresso? "))

			if valorIngresso >= 10:
				validarValor = True
			else:
				print(">>> Atenção: digite um valor numérico com o valor mínimo de 10 reais")
		except Exception as e:
			print(">>> Atenção: digite um valor numérico")
		
def menu():
	global cpf
	limparTela()
	validarOpcao = False
	while validarOpcao == False:
		print("*** Menu ***")
		print("1. Realizar venda")
		print("2. Listar devedores")
		print("3. Listar compradores")
		print("4. Pagar débito (devedores)")
		print("5. Mostrar valor arrecadado pelo evento")

		opcao = int(input("Escolha a opção: "))

		if opcao==1 or opcao==2 or opcao==3 or opcao==4 or opcao==5:
			validarOpcao = True

		if opcao==1:
			realizarVenda()
		elif opcao==2:
			listarDevedores(True)
		elif opcao==3:
			listarCompradores()
		elif opcao==4:
			pagarDebito()
		elif opcao==5:
			mostrarValorArrecadado()
		else:
			print("Opção inválida!")

def pagarDebito():
	limparTela()
	listarDevedores(False)

	print("*** Pagar débito ***")
	cpf = 0
	isCpfValido = False
	
	while isCpfValido == False:
		try:
			cpf = int(input("Digite o número do CPF: "))
			isCpfValido = validarCPF(cpf)

			if isCpfValido == False:
				print(">>> Atenção: Digite um CPF válido")
		except Exception:
			print(">>> Atenção: CPF deve ser numérico")

	if cpf in listaDevedores:
		listaDevedores.remove(cpf)
		print(">>> Dívida foi quitada!")
	else:
		print(">>> Este CPF não possui dívida")

	opcao = int(input("Escolha [1] para voltar ao menu: "))
	if(opcao==1):
		menu()


def realizarVenda():
	limparTela()
	global valorVendas
	isCpfValido = False
	print("*** Realizar Venda ***\n")
	
	try:
		while isCpfValido==:False
			cpf = int(input("Digite o número do CPF: "))
			isCpfValido = validarCPF(cpf)

			if isCpfValido == False:
				realizarVenda()

			if cpf in listaDevedores:
				print(">>> Atenção: Está devendo")
				opcao = int(input("Escolha [1] para pagar o que está devendo: "))
				if opcao==1:
					pagarDebito(cpf)
				else:
					print(">>> Atenção: não pode comprar um novo ingresso")
			else:
				print("Venda efetuada com sucesso!")
				listaCompradores.append(cpf)
				valorVendas = valorVendas+valorIngresso
				menu()
	except Exception as e:
		menu()


def listarDevedores(inicio):
	global listaDevedores
	
	if(inicio==True):
		limparTela()

	print("*** Lista de Devedores ***\n")
	for x in range(0, len(listaDevedores)):
		print(listaDevedores[x])

	try:
		opcao = int(input("Escolha [1] para voltar ao menu: "))
		if(opcao==1):
			menu()
		else:
			listarDevedores(True)
	except Exception as e:
		listarDevedores(True)


def listarCompradores():
	global listaCompradores
	limparTela()
	print("*** Lista de Compradores ***\n")
	for x in range(0, len(listaCompradores)):
		print(listaCompradores[x])

	try:
		opcao = int(input("Escolha [1] para voltar ao menu: "))
		if(opcao==1):
			menu()
		else:
			listarCompradores()
	except Exception as e:
		listarCompradores()

def mostrarValorArrecadado():
	limparTela()
	print("*** Resumo de vendas ***")
	print(len(listaCompradores), " vendas.")
	print("Valor arrecadado: ",valorVendas)

	try:
		opcao = int(input("Escolha [1] para voltar ao menu: "))
		if(opcao==1):
			menu()
		else:
			mostrarValorArrecadado()
	except Exception as e:
		mostrarValorArrecadado()


def validarCPF(cpf):
	strCpf = str(cpf)

	if len(strCpf)!=11:
		return False
	else:
		return True

definirValor()
menu()