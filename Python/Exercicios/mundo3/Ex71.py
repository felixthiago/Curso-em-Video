import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 76 === Lista de Preços com Tupla
##### Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

from Exercicios.utils import *
clear()

total = []
compras = ("3KG batata", 12.58,
           "1KG Cenoura", 5.69,
           "Chocolate 200g", 8.19,
           "Pizza congelada", 32.00)

for pos in range(0, len(compras)):
    if pos % 2 == 0:
        total.append(compras[pos + 1])
        print(f"{cer} Produto ⮕  {compras[pos]} <{'-~-'*3}> {lg}R${compras[pos + 1]}")
print(f"{cer}O valor total da compra foi ⮕  {lg}R${sum(total)}")
