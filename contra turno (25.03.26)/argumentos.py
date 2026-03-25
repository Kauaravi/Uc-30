def resumo_notas(*notas):
    if not notas:
        return "Você não informou nenhuma nota."

    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)

    maior = notas[0]
    menor = notas[0]

    for nota in notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

    return {
        "Soma das notas": soma,
        "Média": media,
        "Maior nota": maior,
        "Menor nota": menor
    }


resultado = resumo_notas(7, 8.5, 6, 9, 10)

for chave, valor in resultado.items():
    print(f"{chave}: {valor}")