import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 75 === Análise de dados em uma Tupla
##### Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares
from cursoemvideo.utils import *
clear()

c = 0
l = []
pares = []

while c < 3:
    c += 1
    try:
        n = safe_int_input(f"{choice}Digite alguns números para serem adicionados em tupla > ")
    except ValueError:
        print(f"{err} O que foi digitado não se parece com um número !")
        quit()

    l.append(n)
    t = tuple(l)

print(f"{strTime}Os números adicionados foram > {t}")
if t.count(9) > 0:
    print(f"{strTime}A quantidade de vezes que o número 9 apareceu foram > {t.count(9)}")

elif t.count(3) > 0:
    print(f"{strTime}A posição em que apareceu o primeiro valor 3 foi > {t.index(3) + 1}")

for c in range(len(t)):
    if t[c] % 2 == 0:
        pares.append(t[c])
        tPares = tuple(pares)
    c += 1

if pares != []:
    print(f"{strTime}Existem alguns números pares nessa lista > {tPares}", end = "")