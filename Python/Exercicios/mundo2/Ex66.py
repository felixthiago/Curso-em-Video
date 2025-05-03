import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 71 === Simulador de Caixa Eletrônico
##### Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from Exercicios.utils import *
clear()

print(f"{choice} Simulador de Caixa Eletrônico")
v = int(input(f"{choice} Digite o valor total a ser sacado $ > "))

cedulas = [50, 20, 10, 1]

for cedula in cedulas:
    quantidade = v // cedula
    if quantidade > 0:
        print(f"{cer}{b}{quantidade}{reset} cédula(s) de {lg}R$ {cedula}{reset}")
    v %= cedula 