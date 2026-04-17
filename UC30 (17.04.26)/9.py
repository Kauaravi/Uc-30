#Questão 9 - Notas
notas = [6.5, 8.0, 7.5, 5.0, 9.2, 7.0]

contador = 0

for nota in notas:
    if nota > 7:
        contador += 1

print("Quantidade de notas acima de 7:", contador)