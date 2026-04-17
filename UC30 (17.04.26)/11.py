#Questão 11 - Idades
idades = []

for i in range(5):
    idade = int(input(f"Digite a idade {i+1}: "))
    idades.append(idade)

idades.sort()

print("Idades em ordem crescente:", idades)