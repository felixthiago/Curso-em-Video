import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 79 === Valores únicos em uma Lista
##### Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

from cursoemvideo.utils import *
clear()

qtd = safe_int_input(f"{choice} Digite a quantidade de números que deseja adicionar a lista > ")

c = 0
l = []

for c in range(qtd):
    n = safe_int_input(f"{choice} Digite um número para ser adicionado a lista > ")   
    if n not in l:
        l.append(n)
        c += 1
    else:
        print(f"{err}Número já adicionado na lista posteriormente, logo não foi adicionado!")

print(f"{cer}Os números digitados foram > {sorted(l)}")
