import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 67 === Tabuada 3.0
######## Descrição: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo

from Exercicios.utils import *
clear()

try:
    n = int(input(f"{choice} Digite um número para ver a tabuada > "))
except ValueError:
    print(f"{err} O que foi digitado não se parece com um número!")
    quit()

while n > 0:
    print(f"\nTabuada do {n} {reset}")
    for i in range(1, 11):
        print(f"{b} {n}{reset} x {b}{i} {reset}= {b}{n * i} {reset}")
    c = input(f"\n{choice} Deseja ver a tabuada de outro número?(S/N) > ").strip().upper()[0]
    if c == 'N':
        print(f"{err} Você digitou NÃO e não quer mais ver a tabuada, tudo bem!")
        break
    elif c == 'S':
        n = int(input(f"{choice} Digite um número para ver a tabuada > "))
    else:
        print(f"{err} O que foi digitado não se parece com uma opção válida!")
        break

print(f"{la}FIM da Tabuada")
