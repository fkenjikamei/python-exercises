print("Calcular salário do mês")

valor_hora = float(input("Qual o valor da hora: "))
horas_trabalhadas = float(input("Quantas horadas trabalhou no mês? "))


salario_bruto = valor_hora*horas_trabalhadas
imposto_renda = (salario_bruto*11)/100
inss = (salario_bruto*8)/100
sindicato = (salario_bruto*5)/100

salario_liquido = salario_bruto-imposto_renda-inss-sindicato

print("Salario bruto: ",salario_bruto)
print("Salario líquido: ",salario_liquido)
print("Imposto pago: ",imposto_renda)
print("INSS pago: ",inss)
print("Sindicato pago: ",sindicato)