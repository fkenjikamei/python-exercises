def validar_maior_idade(idade):
	if idade>=18:
		return True
	else:
		return False

print("Validacao de idade")
idade = int(input("Digite a idade: "))

assert(True==validar_maior_idade(18))
assert(True==validar_maior_idade(88))
assert(False==validar_maior_idade(17))
assert(3 == 2+1)