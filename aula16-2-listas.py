frutas = ["acerola","jaca", "jambo", "acerola"]
print(frutas)

print("jambo" in frutas)

numeros = [10, 8, 2, [3, 4]]
print(3 in numeros[3])

print("\nAdicionar o mamao")
frutas.append("mamao")
print(frutas)

print("\nRemovendo elementos")
print("Remover elemento 1")
del(frutas[1])
print(frutas)
print("Remover acerola")
frutas.remove("acerola")
print(frutas)