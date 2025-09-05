import os
os.system("cls")



# Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.


print(""" 
      
--------valor das Frutas---------      
Fruta	    Até 5 Kg	     Acima de 5 Kg
Morango	   R$ 2,50 por Kg	R$ 2,20 por Kg
Maçã	   R$ 1,80 por Kg	R$ 1,50 por Kg
""") 

print("")

fruta = str(input("""
                  
                  
---------Digite a fruta que você deseja-------------
                  


Morango
                  

""")).lower()

kilos = float(input("Digite a quantidade de KG de morangos que deseja: "))


match fruta:
    case "morango":
        if kilos <= 5:
            valor_morango = kilos * 2.50
        elif kilos > 5:
            valor_morango = kilos * 2.20

fruta = str(input("""
                  
                  

---------Digite a fruta que você deseja-------------
                  

Maca (Maçã)
                  

""")).lower()

kilos = float(input("Digite a quantidade de KG de maçãs que deseja: "))


match fruta:
    case "maca":
        if kilos <= 5:
            valor_maca = kilos * 1.80
        elif kilos > 5:
            valor_maca = kilos * 1.50

valor_total = valor_morango + valor_maca

if kilos >= 10 or valor_total > 15:
    valor_total *= 0.90

print(f"Valor total a ser pago: R$ {valor_total:.2f}")

            

        