#Aula de Funções

saldo = 0
repetir=True

def exibirSaldo():
	print("Saldo: ", saldo)

def validarValorOperacao(valor):
	if valor<=0:
		print("Valor invalido!")
		return False
	else:
		return True

while repetir:
	print("Sistema Bancario")
	print("1- Saldo")
	print("2- Saque")
	print("3- Deposito")
	print("4- Sair")
	opcao = int(input("Escolha uma opcao: "))

	if opcao==1:
		exibirSaldo()
	elif opcao==2:
		print("Opcao de Saque")
		valorSaque = int(input("Qual o valor a sacar?"))
		if validarValorOperacao(valorSaque):
			saldo -= valorSaque
			exibirSaldo()
	elif opcao==3:
		print("Opcao de Deposito")
		valorDeposito = float(input("Qual o valor a depositar?"))
		if valorDeposito>0:
			saldo += valorDeposito
			exibirSaldo()
		else:
			print("Valor invalido: ", valorDeposito)
	elif opcao==4:
		repetir=False
	else:
		print("Opcao invalida")