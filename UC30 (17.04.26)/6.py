#Questão 6 - Média de temperaturas
temperaturas = []

for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

soma = 0

for t in temperaturas:
    soma += t

media = soma / 7

print("Média das temperaturas:", media)