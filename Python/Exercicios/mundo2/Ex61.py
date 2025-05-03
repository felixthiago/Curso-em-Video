import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Sequência de Fibonacci 
######## Descrição: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo
######## 0 - 1 - 2 - 3 - 4 - 8 - 13 - 21 - 34 - 55 - 89

from Exercicios.utils import *
clear()

termo = int(input(f"""{strTime}Sequência de Fibonacci ~~~ Digite quantos termos deseja mostrar > """))
n1 = 0
n2 = 1
c = 1
print(f"{b} {n1} {reset}→{b} {n2} {reset}→ ", end="")

while c <= termo:
    n3 = n1 + n2
    print(f"{b} {n3} {Fore.RESET}→ ", end='')
    n1 = n2
    n2 = n3
    c += 1

print(f"\n{la}FIM da Sequência de Fibonacci")