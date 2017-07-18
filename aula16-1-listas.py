print("Trabalhando com Listas")

lista_numeros = [1, 10, 20, 30]
print(lista_numeros)

lista_nomes = ["fulano", "ciclano"]
print(lista_nomes)

lista_misturada = ["texto", 10.5, 9]
print(lista_misturada)

listas_juntas = [1000, lista_numeros, lista_nomes, lista_misturada]
print(listas_juntas)


print("\nAcessando valores da lista")
print(lista_numeros[3])
print(lista_nomes[0])
print(lista_misturada[2])
print(listas_juntas[1])
print(listas_juntas[2][1])
print(listas_juntas[-2])