import os 
os.system

#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#Combustível	Quantidade Vendida	Desconto por Litro
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: 
# A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 6,59 e o
#  preço do litro do álcool é R$ 3,79.

preco_alcool = 3.79
preco_gasolina = 6.59


litros = float(input("Digite a quantidade de litros desejada: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()


if tipo == "A":
    if litros <= 25:
        valor = litros * preco_alcool * 0.9 
    else:
        valor = litros * preco_alcool * 0.8  
    print(f"Valor a pagar: R$ {valor:.2f}")

elif tipo == "G":
    if litros <= 25:
        valor = litros * preco_gasolina * 0.85  
    else:
        valor = litros * preco_gasolina * 0.7  

    print(f"Valor a pagar: R$ {valor:.2f}")

else:
    print("Tipo de combustível inválido")
