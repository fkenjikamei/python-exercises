limite_gasto=0
qtd_brinquedos=0

valida_qtd_brinquedos=False
valida_limite_gasto=False

#Recebendo e validando o valor digitado para o limite de gasto
while (valida_limite_gasto==False):
	limite_gasto=float(input("Digite o valor disponível para gastar: "))
	if limite_gasto>=1 and limite_gasto<1000000000:
		valida_limite_gasto=True
	else:
		print(">> Valor inválido")

#Recebendo e validando o valor digitado para a quantidade de brinquedos
while (valida_qtd_brinquedos==False):
	qtd_brinquedos=int(input("Digite a quantidade de brinquedos existentes na loja: "))
	if qtd_brinquedos>0 and qtd_brinquedos<100000:
		valida_qtd_brinquedos=True
	else:
		print(">> Valor inválido, digite novamente.")

lista_brinquedos=[]
lista_comprados=[]
valor_compra=0.0

#Recebendo e valindo o valor digitado para o limite de gasto
for x in range(0,qtd_brinquedos):
	valor_brinquedo=float(input("Digite o valor do brinquedo: "))
	if valor_brinquedo >=1 and valor_brinquedo <= 1000000000:
		lista_brinquedos.append(valor_brinquedo)
	else:
		print(">> Digite um número entre 1 e 1000000000!!")
		x-=1

#Ordenando a lista de brinquedos pelo preço
lista_brinquedos=sorted(lista_brinquedos)

#Adicionando brinquedos na lista de comprados
for m in range(0,len(lista_brinquedos)):
	produto=lista_brinquedos[m]
	if limite_gasto>0 and limite_gasto>=produto:
		limite_gasto=limite_gasto-produto
		lista_comprados.append(produto)

print("Eles compraram ",len(lista_comprados),"brinquedo(s) no valor de cada um em: ",lista_comprados)