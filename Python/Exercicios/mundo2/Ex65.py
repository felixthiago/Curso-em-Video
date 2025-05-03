import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 70 === Estatisticas em Produtos
##### Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

from Exercicios.utils import *
clear()

p = {}
qtd = int(input(f"{choice} Quantos produtos deseja analisar? > "))
i = 0
gastos = []
gastoMaior = []

for i in range(1, qtd + 1):
    try:
        productName = input(f"{choice} Digite o nome do produto > ")
        productPrice = int(input(f"{choice} Digite o preço do produto R$ > "))
        if productPrice > 1000:
            gastoMaior.append(productPrice)

        gastos.append(productPrice)
    except ValueError:
        print(f"{err} O que foi digitado não se parece com um nome!")
        quit()
    p.update(
    {
        f'p{i}': {
            'Nome': f'{productName}',
            'Preco': {productPrice}
        }
    }
    )
print(f"{cer} A soma do total das compras é de > R${sum(gastos)}")
print(f"{cer} O produto mais barato dessa lista custou > R${min(gastos)}")
if len(gastoMaior) != 0:
    print(f"{err}O total de produtos que custam mais de R$1000 é de: {len(gastoMaior)}")
