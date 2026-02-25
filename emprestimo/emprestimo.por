programa {
    funcao inicio() {
        real valorCasa, salario, prestacao
        inteiro anos, meses        
        escreva("Qual seu salario: ")
        leia(valorCasa)

        escreva("Em quantos anos você deseja pagar: ")
        leia(anos)

        meses = anos * 12
        prestacao = valorCasa / meses

        escreva("O valor da prestação é", prestacao)

        se(prestacao <= salario * 0.30) {
            escreva("EMpréstimo aprovado \n")
            }
            senao {
                escreva("Empréstimo não aprovado \n")
            }
        
    }
}