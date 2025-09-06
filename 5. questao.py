import os
os.system("cls")


# faça um programa que leia um código de operação (+, -, *, ou /) e também dois valores inteiros A e B. O programa deve calcular o resultado da operação escolhida aplicada a A e B.
#  Por exemplo, se a operação escolhida foi * e A = 1 e B = 3, o programa deve fornecer como resultado o valor de 1 * 3, que é 3.


A = int(input("Digite um numero: "))
B = int(input("Digite o segundo numero: "))



operacao= str(input("Digite a operação desejada +, /, -, *: "))


soma = (A + B)
subtracao = (A - B)
divisao = (A / B)
multiplicacao = (A * B)

if B != 0:
    divisao = (A / B)
else:
    divisao = 0

match operacao:
    case "+":
        print(f"O resultado da soma: {soma}")
    case "-":
        print(f"O resutado da subtração: {subtracao}")
    case "/":
        print(f"O resultado da sua divisão: {divisao}")
    case "*":
        print(f"O resultado da sua multiplicação: {multiplicacao}")

