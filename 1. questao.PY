import os
os.system("cls") 

# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C, caso contrário, imprima que A + B é maior que C.

A = float(input("Digite um número para a soma: "))

B = float(input("Digite o segundo número para soma: "))

C = float(input("Diga o terceiro número: "))

soma = A + B

if soma < C:
    print(f"O resultado da soma: ({soma: .2f}) é menor que {C}")

elif soma > C:
    print(f"O resultado da soma: ({soma: .2f}) é maior que {C}")