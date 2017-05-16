#Se for menor de idade, tem que 
#ter autorização

idade = 15
isAutorizacao = False

if idade >= 18:
	print("Maior de idade")
	print("Pode entrar!")
	print("Tem idade igual :",idade)
elif idade < 18 and isAutorizacao == True:
	print("Menor de idade")
	print("Entra, tem autorizacao!")
else:
	print("Menor de idade")
	print("Sem autorizacao")

print("Fim")