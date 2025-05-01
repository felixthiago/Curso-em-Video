import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === P.A
######## Descrição: "Programa simples é dado a razão e o termo de uma p.a e ela é feita"

from Exercicios.utils import *

try:
    distancia = int(input(f'{choice} Até onde devo contar essa P.A? > '))
    termo = int(input(f'{choice} Digite o primeiro termo para uma P.A > '))
    razao = int(input(f'{choice} Digite a razão para uma P.A > '))
except ValueError:
    print(f'{err} O que foi digitado não se parece com um número! ')
    quit()

print(f'\n{strTime} Aqui está a P.A em questão! \n')

for c in range(termo, distancia + razao, razao):
    print(f'{Fore.GREEN}{c}{Fore.RESET}, ', end='')
