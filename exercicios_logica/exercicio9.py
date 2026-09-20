"""Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno.
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.
Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o ponto decimal
 e com um espaço em branco antes e depois da igualdade. Assim como todos os problemas,
não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error"."""

def media():

    while True:

        try:

            valor_A = int(input("Digite o primeiro valor: "))
            valor_B = int(input("Digite o segundo valor: "))
            valor_C = int(input("Digite o terceiro valor: "))

        except ValueError:
            print("Digite um numero valido")
            continue

        if valor_A < 0 or valor_B < 0 or valor_C < 0:
            print("Digite um valor positivo.")
        else:
            media = (valor_A + valor_B + valor_C)/3
            print(f"A média é {media}")
            break

media()


