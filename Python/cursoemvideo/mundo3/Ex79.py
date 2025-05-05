import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 84 === Lista composta e análise de dados
##### Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
### A) Quantas pessoas foram cadastradas.
### B) Uma listagem com as pessoas mais pesadas. 
### C) Uma listagem com as pessoas mais leves.

from cursoemvideo.utils import *
clear()

user = list()
pesos = list()
u = list()
qtd = safe_int_input(f"{choice}Digite quantos usuarios deseja cadastrar > ")
c = 0
a = 0

while c < qtd:
    print("\n")

    u.append(safe_str_input(f"{choice}Username > "))
    u.append(safe_int_input(f"{choice}Idade > "))
    u.append(safe_float_input(f"{choice}Peso(KG) > "))
    user.append(u[:])
    u.clear()
    c += 1

i = 0
for c in range(qtd):
    pesos.append(user[c][2])

print(f"\n{cer}Foram cadastrados {len(user)} Usuarios no banco de dados")
print(f"{cer}A pessoa mais pesada da lista pesa {max(pesos)}KG")
print(f"{cer}A pessoa mais leve dessa lista pesa {min(pesos)}KG")