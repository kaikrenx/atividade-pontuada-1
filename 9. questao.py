import os
os.system

#Uma financeira usa o seguinte critério para conceder empréstimos: o valor total do empréstimo deve ser até dez vezes
#  o valor da renda mensal do solicitante, e o valor da prestação deve ser no máximo 30% da renda mensal do solicitante.
#  Escreva um programa que leia a renda mensal de um solicitante, o valor total do empréstimo solicitado e o
#  número de prestações que o solicitante deseja pagar e informe se o empréstimo pode ou não ser concedido.



salario = float(input("Digite o seu sálario para fazer o empréstimo: "))

emprestimo = salario * 10 


print("")
print(f"Seu empréstimo pode ser de até {emprestimo: .2f}")
print("")

emprestimo_solc = float(input("Digite o valor que deseja pegar de empréstimo: "))


if emprestimo < emprestimo_solc:
    
    print("Valor indevido, tente outro valor")

else:
    
    prestacoes = int(input("Digite o número de prestações desejadas (até 12): "))

valor_parcela = emprestimo_solc / prestacoes


if valor_parcela > salario * 0.3:
        print(f"Empréstimo negado, o valor da parcela ultrapassa 30% do salário.")
else:
        match prestacoes:
            case 1:
                print(f"1x de R$ {emprestimo_solc:.2f}")
            case 2:
                parcela = emprestimo_solc / 2
                print(f"2x de R$ {parcela:.2f}")
            case 3:
                parcela = emprestimo_solc / 3
                print(f"3x de R$ {parcela:.2f}")
            case 4:
                parcela = emprestimo_solc / 4
                print(f"4x de R$ {parcela:.2f}")
            case 5:
                parcela = emprestimo_solc / 5
                print(f"5x de R$ {parcela:.2f}")
            case 6:
                parcela = emprestimo_solc / 6
                print(f"6x de R$ {parcela:.2f}")
            case 7:
                parcela = emprestimo_solc / 7
                print(f"7x de R$ {parcela:.2f}")
            case 8:
                parcela = emprestimo_solc / 8
                print(f"8x de R$ {parcela:.2f}")
            case 9:
                parcela = emprestimo_solc / 9
                print(f"9x de R$ {parcela:.2f}")
            case 10:
                parcela = emprestimo_solc / 10
                print(f"10x de R$ {parcela:.2f}")
            case 11:
                parcela = emprestimo_solc / 11
                print(f"11x de R$ {parcela:.2f}")
            case 12:
                parcela = emprestimo_solc / 12
                print(f"12x de R$ {parcela:.2f}")

            case _:
                print("Opção inválida")






