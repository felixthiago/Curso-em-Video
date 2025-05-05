import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 82 === Dividindo valores em várias listas
##### Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

from cursoemvideo.utils import *
clear()

pares = []
impares = []

qtd = safe_int_input(f"{choice}Digite uma quantidade de números para serem alocados em uma lista > ")

c = 0
while c < qtd:
    n = safe_int_input(f"{choice}Digite alguns números > ")
    c += 1
    if n % 2 == 0:
        pares.append(n)
    elif n % 3 == 0:
        impares.append(n)
    else:
        print(f"{err}Número inválido!")
        quit()

print(f"{strTime}Foram digitados {len(pares) + len(impares)} números ao total e {len(pares)} deles são pares! > {pares}\n{strTime}Já {len(impares)} deles são impares! > {impares}")

