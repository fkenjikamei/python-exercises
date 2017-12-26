texto = "abcdefabcghiklmnabdiuabcoe"
encontrar = "abc"

tamanhoTexto = len(texto)
tamanhoEncontrar = len(encontrar)

contEncontrados = 0


print("Foram encontrados ", texto.count("abc"), " vezes a palavra ",encontrar)

novoTexto = texto.replace("abc", "111")

print(novoTexto)

frase = "Eu estudo programacao Todos os dias"
print(frase.split())

print(frase.upper())
print(frase.lower())
print(frase.lower().capitalize())
print(frase.title())
print(frase.swapcase())

print("Frase toda maiúscula? ", frase.isupper())
print("Frase toda maiúscula? ", frase.islower())

print("Sem caracteres especiais? ", frase.isa1num())
print("Apenas letras? ", frase.isalpha())
print("Apenas digitos? ", frase.isdigit())
print("Apenas espaços? ", frase.isspace())
