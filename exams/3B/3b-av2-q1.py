x=0
y=0
isXValido = False
isYValido = False

while(isXValido == False):
	x = int(input("Digite um número positivo de 1 a 100, para definir o INÍCIO do intervalo: "))
	if(x >= 0):
		isXValido = True
	else:
		print("\n>> Digite um número positivo")

while(isYValido == False):
	y = int(input("Digite um número positivo para definir o FIM do intervalo: "))
	if(y > 0 and y > x):
		isYValido = True
	else:
		print("\n>> Digite um número positivo e maior do que o início do intervalo")

for z in range(x,y+1):
	if not(z%10==0):
		if(z>10):
			za = z//10
			if(z%za==0):	
				print(z)