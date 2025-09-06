import os
os.system("cls")



# Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. 
# Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que:
# Se quantidade <= 5, o desconto será de 2%.
# Se quantidade > 5 e quantidade <= 10, o desconto será de 3%.
# Se quantidade > 10, o desconto será de 5%.



produto = str(input("""
------Digite o nome do produto-----

pc
celular
                    
                    
""")).lower()

qntd = float(input("Digite a quantidade: ( 2 ou 3)"))

if qntd <= 5:
    desconto = valor_total * 0.02
elif qntd > 5 and qntd <= 10:
    desconto = valor_total * 0.03
elif qntd > 10:
    desconto = valor_total * 0.05

valor_descontado = valor_total - desconto

print(f"O valor total da sua compra foi de: R${valor_total: .2f} sem desconto")
print("")
print(f"Esse é o valor total com desconto: R${valor_descontado: .2f}")
