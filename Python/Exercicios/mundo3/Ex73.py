import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 78 === Maior e Menor valores na Lista
##### Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

from Exercicios.utils import *
clear()
c = 0
l = []

try:
    qtd = int(input(f"{choice}Digite a quantidade de números que deseja ler > "))
    while c < qtd:
        n = int(input(f"{strTime}Digite um número para ser colocado em uma lista > "))
        l.append(n)
        c += 1
    print(f"{cer} Dentre os números digitados os maiores e menores foram > {max(l)}/{min(l)}")

except ValueError:
    print(f"{err}O que foi digitado não se parece com um número")
    quit()

