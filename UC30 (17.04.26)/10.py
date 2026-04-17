#Questão 10 - vogais
frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print("Quantidade de vogais:", contador)