total_segundos = int(input("Digite os segundos: "))

minutos = total_segundos//60%60
segundos = total_segundos%60
horas = total_segundos//3600%24
dias = total_segundos//(3600*24)

print("")
print("> Dias:", dias)
print("> Horas:", horas)
print("> Minutos:", minutos)
print("> Segundos:", segundos)
print("")