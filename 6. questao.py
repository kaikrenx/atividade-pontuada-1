import os
os.system("cls")

#Escreva um programa que leia do teclado as duas notas de um aluno, calcule e exiba a média aritmética das notas.
#  O programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno esteja aprovado (média superior ou igual a 6,0); caso a média esteja entre 4,1 e 5,9,
#  o aluno está em recuperação; caso a média seja inferior a 4,0, o aluno será reprovado.


aluno = str(input("Digite o nome do aluno: "))

Nota_1= float(input(f"Digite a primeira nota: "))
Nota_2= float(input(f"Digite a segunda nota: "))



media =  (Nota_1 + Nota_2) / 2 # calcular media

if media >= 6: 
    print(f" {aluno} Você foi aprovado, Parabéns, a seguir a nota: {media} ")
elif media >= 4.1 and media <= 5.9:
    print(f" {aluno} Você está em recuperação, a seguir a nota: {media} ")
elif media <= 4:
   print(f" {aluno} Você foi reprovado, a seguir a nota: {media} ")