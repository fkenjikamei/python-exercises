idade = int(input("Digite a idade: "))
permissao = input("Tem permissao? (Sim ou Nao) ")

print("")
print("and")
print(idade >= 18 and permissao=="Sim")

print("")
print("or")
print(idade >= 18 or permissao==	"Sim")

print("")
print("not")
print(not(idade >= 18))

print("not 2")
print(not(3<4))