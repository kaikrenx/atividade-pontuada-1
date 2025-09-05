import os 
os.system("cls")


#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
# Caso o sexo seja “F” e o estado civil seja “CASADA”, solicitar o tempo de casada (em anos). Por fim, mostre os dados do usuário.

nome = str(input("Digite seu nome: ")).lower()
genero = str(input(""" 
------------ Digite seu gênero-------------

Masculino
Feminino
                   

""")).lower()

estado_civil = str(input("""
--------Digite seu estado civil--------
                         
solteiro(a)
casado(a)
                         
""")).lower()


if genero == "feminino":

    match estado_civil:

        case "casada":

            anos = float(input("Quantos anos de casado(a) você possui? "))

            print(f"""
 ---------- TABELA ----------

Nome: {nome}    
genero: {genero}
estado civil: {estado_civil}
Anos de casada: {anos}
    
""")
        
        case "solteira":
    
            print(f"""
 ---------- TABELA ----------

Nome: {nome}    
genero: {genero}

""")
        case _: 
            print("genero invalido")


elif genero == "masculino":

    print(f"""
 ---------- TABELA ----------

Nome: {nome}    
genero: {genero}

""")




    