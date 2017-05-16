#Questão 4
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra=='a' or letra=='A' or letra=='e' or letra=='E' or letra=='i' or letra=='I' or letra=='o' or letra=='O' or letra=='u' or letra=='U':
	print("Vogal")
elif letra=='b' or letra=='B' or letra=='c' or letra=='C' or letra=='d' or letra=='D' or letra=='f' or letra=='F' or letra=='g' or letra=='G' or letra=='h' or letra=='H' or letra=='j' or letra=='J' or letra=='k' or letra=='K' or letra=='l' or letra=='L' or letra=='m' or letra=='M' or letra=='n' or letra=='N' or letra=='p' or letra=='P' or letra=='q' or letra=='Q' or letra=='r' or letra=='R' or letra=='s' or letra=='S' or letra=='t' or letra=='T' or letra=='v' or letra=='V' or letra=='w' or letra=='W' or letra=='x' or letra=='X' or letra=='y' or letra=='Y' or letra=='z' or letra=='Z':
	print("Consoante")
else:
	print("Não é uma letra válida")