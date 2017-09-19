saldo = 0

def depositar(valor):
	if valor > 0:
		global saldo
		saldo += valor
	return saldo

assert(depositar(100) == 100)
saldo=0
assert(depositar(200) == 200)
saldo=0
assert(depositar(300) == 300)
saldo=0

valor = float(input("Digite o valor a depositar: "))
depositar(valor)
print("Saldo: ",saldo)