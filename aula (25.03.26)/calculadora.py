def calculadora():
    while True:
        print("\nCalculadora")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        opcao = input("O que você deseja fazer? ")

        if opcao == "0":
            print("Até mais!")
            break

        if opcao in ["1", "2", "3", "4"]:
            try:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))

                if opcao == "1":
                    print(f"Resultado: {n1 + n2}")
                elif opcao == "2":
                    print(f"Resultado: {n1 - n2}")
                elif opcao == "3":
                    print(f"Resultado: {n1 * n2}")
                elif opcao == "4":
                    if n2 == 0:
                        print("Não dá pra dividir por zero")
                    else:
                        print(f"Resultado: {n1 / n2}")

            except ValueError:
                print("Digite apenas números válidos.")
        else:
            print("Opção inválida, tente novamente.")


calculadora()