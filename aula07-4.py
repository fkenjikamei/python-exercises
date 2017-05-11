#Permissao para Viajar do pais

idade = int(input("Digite a idade: "))
tem_permissao_governo = input("Permissao do governo? S-Sim, N-Nao ")

#Para sair do pais, tem que ser maior de idade
#e ter permissão do governo
print((idade>=18) and (tem_permissao_governo == "S" or tem_permissao_governo == "s"))