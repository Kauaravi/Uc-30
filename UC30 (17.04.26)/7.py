#Questão 7 - Vendas
vendas = [10, 15, 20, 7, 8, 12]

soma = 0

for valor in vendas:
    if valor % 2 == 0:
        soma += valor

print("Soma dos valores pares:", soma)