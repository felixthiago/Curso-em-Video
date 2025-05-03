import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio(60 e 61) === Progressão Aritmética v2.0 & 3.0
######## Descrição: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
# + Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos

from Exercicios.utils import *
clear()

try:
    qtd = int(input(f"{choice} Quantos termos você quer mostrar? > "))
    termo = int(input(f"{choice} Digite o primeiro termo da P.A > "))
    razao = int(input(f"{choice} Digite a razão da P.A > "))
except ValueError: 
    print(f"{err} O que foi digitado não se parece com um número! ")
    quit()

count = 1
total = 0
mais = qtd

while mais != 0:
    total = total + mais
    while count <= total:
        print(f"{b} {termo} {Fore.RESET}> ", end='')
        count += 1
        termo += razao
    mais = int(input(f"\n{choice} Deseja mais termos? [0 para parar] > "))

print(f"{la}FIM da P.A")