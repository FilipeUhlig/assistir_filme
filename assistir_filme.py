"""
Programa: assistir_filme
Descrição: Este programa verifica a idade de uma pessoa e se ela pode ou não assistir ao filme.
Autor: F
Data : 23/06/2023
Versão: 0.0.1
"""

#Atribuição de variáveis



i = 0
nome = 0

#Entrada de dados

nome = input("Qual o seu nome? ")
i = int(input("Qual sua idade? ")) 


#Processamento de dados

n = nome.capitalize()

if i >= 18:
    print(f"{n} pode assistir ao filme.")

else:
    print(f"{n} não pode assistir ao filme.")


#Saida de dadaos