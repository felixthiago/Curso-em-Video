import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === P.A
######## Descrição: "Programa simples é dado a razão e o termo de uma p.a e ela é feita"

from cursoemvideo.utils import *

distancia = safe_int_input(f'{choice} Até onde devo contar essa P.A? > ')
termo = safe_int_input(f'{choice} Digite o primeiro termo para uma P.A > ')
razao = safe_int_input(f'{choice} Digite a razão para uma P.A > ')

print(f'\n{strTime} Aqui está a P.A em questão! \n')

for c in range(termo, distancia + razao, razao):
    print(f'{Fore.GREEN}{c}{Fore.RESET}, ', end='')
