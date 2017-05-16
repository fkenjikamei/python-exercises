valor_hora = float(input("Qual o valor da hora: "))
horas_trabalhadas = float(input("Quantas horas trabalhou? "))

salario_bruto = (horas_trabalhadas*valor_hora)
imposto_renda = (salario_bruto*11)/100
inss = (salario_bruto*8)/100
sindicato = (salario_bruto*5)/100

salario_liquido = salario_bruto - imposto_renda - inss - sindicato


print "Salario liquido: ", salario_liquido