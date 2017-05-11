#Conversao de Tempo

#1. De minutos para segundos
#2. De segundos para minutos
#3. De minutos para horas
#4. De horas para minutos

minutos = int(input("Digite a quantidade em minutos: "))
minutos_para_segundos = minutos*60
print(minutos, "equivalem a", minutos_para_segundos, "segundos")

segundos = int(input("\nDigite a quantidade em segundos: "))
segundos_para_minutos = segundos/60
print(segundos, "equivalem a", segundos_para_minutos, "minutos")

minutos = int(input("\nDigite a quantidade em minutos: "))
minutos_para_horas = minutos/60
print(minutos, "equivalem a", minutos_para_horas, "hora(s)")

horas = int(input("\nDigite a quantidade em horas: "))
horas_para_minutos = horas*60
print(horas, "equivalem a", horas_para_minutos, "minutos(s)")
