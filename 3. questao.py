import os
os.system("cls")

# Faça um algoritmo que leia dois valores inteiros A e B. Se os valores forem iguais, deverá se somar os dois; caso contrário, multiplique A por B. 
# Ao final de qualquer um dos cálculos, deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

A = int(input("Digite um número: "))

B = int(input("Digite o segundo número: "))


if A == B:

    C = A + B 
    
    print(f"A variável C resultante da soma dos numeros é: {C: .2f}")

else:

    C = A * B

    print(f"A variável C resultante da multiplicação dos numeros é: {C: .2F}")




