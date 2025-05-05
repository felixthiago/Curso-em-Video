import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 80 === Lista ordenada sem repetições
##### Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela

from cursoemvideo.utils import *
clear()

l = []

qtd = safe_int_input(f"{choice}Digite a quantidade de números para serem adicionados em uma lista > ")

for c in range(qtd):
    n = safe_int_input(f"{choice}Digite algum número > ")
    if c == 0 or n > l[-1]:
        l.append(n)
    else:
        pos = 0
        while pos < len(l):
            if n <= l[pos]:
                l.insert(pos, n)
                break
            pos += 1

print(f"{cer}Lista de números ordenadas > {l}")

