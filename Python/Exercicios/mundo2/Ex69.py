import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 74 === Maior e menor valores em Tupla
##### Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from Exercicios.utils import *
clear()

c = 0
l = []

for c in range(0, 5):
    from random import randint
    n = randint(0, 5)
    l.append(n)
    t = tuple(l)
    c += 1

print(f"{cer}Foram aleatoriamente gerados 5 números > {t}")
print(f"{cer}O maior número dessa lista é > {max(t)}")
print(f"{cer}O menor número dessa lista é > {min(t)}")

