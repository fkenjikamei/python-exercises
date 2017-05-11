print("Lanchonete")

qtd_suco_laranja = int(input("Quantidade de suco? "))
qtd_sanduiche = int(input("Quantidade de sanduiches? "))
qtd_brigadeiro = int(input("Quantidade de brigadeiro? "))

total_suco_laranja = 3.0 * qtd_suco_laranja
total_sanduice = 5.0 * qtd_sanduiche
total_brigadeiro = 1.0 * qtd_brigadeiro

total_venda = total_suco_laranja+total_sanduice+total_brigadeiro

print("Valor Total = ", total_venda)