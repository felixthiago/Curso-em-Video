import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Criando um Menu de Opções
######## Descrição: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from Exercicios.utils import *
clear()
try:
    n = int(input(f"{choice} Digite um número para o calculo do fatorial > "))
except ValueError:
    print(f'{err} O que foi digitado não se parece com um número!')
    quit()

for n in range(1, n + 1):
    fatorial = 1
    for c in range(1, n + 1):
        fatorial *= c
        
print(f"{cer} O fatorial de {n} é {fatorial}")

