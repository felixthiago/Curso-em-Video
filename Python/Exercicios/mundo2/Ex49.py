import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Tabuadas
######## Descrição: "Programa simples onde dado um número pelo usuario e feito a tabuada até ele"

from Exercicios.utils import *


try:
    number = int(input(f'{choice} Digite o número para realizar a tabuada > '))
    quantia = int(input(f'{choice} Até que número devo criar a tabuada? > '))
except ValueError:
    print(f'{err} O que foi digitado não e um número! ')
    quit()


print(f"\n{strTime}Tabuada do {number} até o {quantia}")

for t in range(1, quantia + 1):
    soma = number * t
    print(f'{cer} {number}{Fore.BLUE} * {Fore.RESET}{t} == {soma}') 
print(f'\n{strTime}Fim da tabuada do {number}')