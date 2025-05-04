import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 77 === Contando vogais em Tupla
####### Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

from Exercicios.utils import *
clear()

palavras = ("python", "amo", "essa", "linguagem", "boa", "noite")

for c in range(len(palavras)):
    print(f"\n{choice}Palavra {palavras[c].upper()} encontramos as vogais > ", end = "")
    for letra in palavras[c]:
        if letra.upper() in 'AEIOU':
            print(f"[{letra.upper()}]", end = "") 
