saldo = 0

def depositar(valor):
	print("*** DEPÓSITO ***")
	global saldo
	saldo = saldo + valor

def exibirSaldo():
	global saldo
	print("*** SALDO ***")
	print(saldo)

def sacar(valor):
	global saldo
	print("*** SAQUE ***")

	if valor <= saldo:
		saldo = saldo - valor
		print("Saque efetuado com sucesso!")
		print("Retire seu dinheiro")
	else:
		print("Saldo insuficiente")