#Questão 4 - IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        return "Magro"
    elif imc <= 24.9:
        return "Normal"
    elif imc <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"


try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    resultado = calcular_imc(peso, altura)
    print("Classificação:", resultado)

except:
    print("Entrada inválida! Digite números válidos.")