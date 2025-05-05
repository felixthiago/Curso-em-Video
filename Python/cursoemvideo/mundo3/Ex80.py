import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 85 === Lista composta e análise de dados
##### Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

from cursoemvideo.utils import *
clear()

qtd = safe_int_input(f"{choice}Digite a quantidade de valores que deseja cadastrar > ")
c = 0
l = [[], []]

while c < qtd:
    c += 1
    n = safe_int_input(f"{choice}Digite o {c}° valor > ")
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)

print(f"{strTime}Pares >> {l[0]}")
print(f"{strTime}Impares >> {l[1]}")
print(f"{strTime}Em ordem crescente {sorted(l)}")