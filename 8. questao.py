import os
os.system("cls")

#Em uma loja de CD's existem apenas quatro tipos de preços que estão associados a cores.
#  Assim, os CD's que ficam na loja não são marcados por preços e sim por cores.
#  Desenvolva um algoritmo que, a partir da entrada da cor, o software mostre o preço.
#  A loja está atualmente com a seguinte tabela de preços:

#Cor	     Preço
#Verde	    R$ 10,00
#Azul	    R$ 20,00
#Amarelo	R$ 30,00
# Vermelho	R$ 40,00

cor = str(input("""
      
---------Digite a cor do CD que deseja saber o preço ---------
      
Verde
Azul
Amarelo
Vermelho

""")).lower()

match cor:
    case "verde":
        print(f"O valor do CD da cor que você selecionou é: R$ 10,00")

    case "azul":
        print(f"O valor do CD da cor que você selecionou é: R$ 20,00")

    case "amarelo":
        print(f"O valor do CD da cor que você selecionou é: R$ 30,00")

    case "vermelho":
        print(f"O valor do CD da cor que você selecionou é: R$ 40,00")

    case _:
        print("Cor inválida! Digite uma das opções listadas.")
