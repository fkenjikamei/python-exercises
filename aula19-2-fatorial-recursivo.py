#fatorial de um numero, é a multiplicacao de todos os numeros 1 até o proprio numero

#5! = 5x4x3x2x1
#6! = 6x5x4x3x2x1

def fatorial(numero):
	if numero == 1:
		return 1
	else:
		return numero*fatorial(numero-1)

numero = int(input("Digite um número: "))
print(fatorial(numero))

assert(1==fatorial(1))
assert(2==fatorial(2))
assert(6==fatorial(3))
assert(24==fatorial(4))
assert(120==fatorial(5))