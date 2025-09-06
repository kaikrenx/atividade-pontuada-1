import os
os.system("cls")



# Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.


print(""" 
      
--------valor das Frutas---------      
Fruta	            Até 5 Kg	     Acima de 5 Kg
Morango	   R$ 2,50 por Kg	    R$  2,20 por Kg
Maçã	         R$ 1,80 por Kg     R$ 1,50 por Kg
""") 

print("")

fruta = str(input("Digite a fruta que você deseja (Morango): ")).lower()
kilos_morango = float(input("Digite a quantidade de KG de morangos que deseja: "))

match fruta:
    case "morango":
        if kilos_morango <= 5:
            valor_morango = kilos_morango * 2.50
        else:
            valor_morango = kilos_morango * 2.20
    case _:
        valor_morango = 0

fruta = str(input("Digite a fruta que você deseja (Maca): ")).lower()
kilos_maca = float(input("Digite a quantidade de KG de maçãs que deseja: "))

match fruta:
    case "maca":
        if kilos_maca <= 5:
            valor_maca = kilos_maca * 1.80
        else:
            valor_maca = kilos_maca * 1.50
    case _:
        valor_maca = 0

valor_total = valor_morango + valor_maca
peso_total = kilos_morango + kilos_maca

if peso_total >= 10 or valor_total > 15:
    valor_total *= 0.90

print(f"Valor total a ser pago: R$ {valor_total:.2f}")

            

        
