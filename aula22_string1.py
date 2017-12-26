import string

texto="Instituto Federal de Alagoas"
print(texto[2])

print("Tamanho: ",len(texto))

print("Fatiar de 3 a 10: ", texto[3:11])
print("Fatiar de 30 a 40: ", texto[:40])

print(texto.find("de"))


fruta = "maracuja"
print(fruta.find("ara"))
print(fruta.find("racu", 2))
print(fruta.find("na", 2, 4))