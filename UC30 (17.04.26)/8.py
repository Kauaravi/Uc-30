#Questão 8 - Desconto
valor = float(input("Digite o valor da compra: "))

if valor > 500:
    desconto = valor * 0.20
elif valor >= 200:
    desconto = valor * 0.10
else:
    desconto = 0

preco_final = valor - desconto

print("Preço final:", preco_final)