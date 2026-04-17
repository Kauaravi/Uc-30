#Questão 12 - Calculadora
while True:
    print("\n--- Calculadora ---")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Encerrando...")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = num1 + num2
            print("Resultado:", resultado)

        elif opcao == "2":
            resultado = num1 - num2
            print("Resultado:", resultado)

        elif opcao == "3":
            resultado = num1 * num2
            print("Resultado:", resultado)

        elif opcao == "4":
            if num2 == 0:
                print("Não é possível dividir por zero!")
            else:
                resultado = num1 / num2
                print("Resultado:", resultado)

        else:
            print("Opção inválida!")

    except:
        print("Entrada inválida! Digite números válidos.")