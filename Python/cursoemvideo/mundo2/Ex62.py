import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Tratando vários valores e maior e menor valores
######## Descrição 64 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
######## + Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

from cursoemvideo.utils import *
clear()

n = safe_int_input(f"{choice} Digite um número inteiro qualquer > ")

l = []

while True:
    n = safe_int_input(f"{choice} Digite um número inteiro qualquer > ")
    l.append(n)
    c = safe_int_input(f"{choice} Deseja continuar? [S/N] > ").strip().upper()[0]

    if c == 'N':
        break
    elif c == "S":
        l.append(n)
        continue
    else:
        print(f"{err} O que foi digitado não se parece com uma opção válida!")
        break

print(f"{strTime} Você digitou {g}{len(l)}{reset} números, parabéns! soma deles é {g}{sum(l)}{reset} a média é {g}{round(sum(l) / len(l))}{reset} e o maior de todos é {g}{max(l)}{reset}")