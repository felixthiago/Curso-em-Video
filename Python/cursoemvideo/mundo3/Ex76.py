import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 81 === Lista ordenada sem repetições
##### Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

from cursoemvideo.utils import *
clear()

qtd = safe_int_input(f"{choice}Digite a quantidade para uma lista > ")
l = []

for c in range(qtd):
    n = safe_int_input(f"{choice}Digite algum número > ")
    l.append(n)

print(f"{cer}A quantidade de números digitados foram > {len(l)}")
if 5 in l:
    print(f"{cer}O número 5 foi digitado e está na posição {l.index(5) + 1}° da lista")
else:
    print(f"{cer}O número 5 não foi digitado e não está na lista!")

l.sort(reverse = True)
print(f"{cer}Aqui está a lista em formato decrescente > {l}")