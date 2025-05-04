import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Contagem Regressiva
######## Descrição: "Simples Programa onde o usuario manda um número para o programa e o mesmo faz uma contagem regressiva dele"

from time import sleep
from cursoemvideo.utils import *
clear()

n = safe_int_input(f'{choice}Até que número devo contar? > ')

for count in range(n, -1, -1):
    print(f"{cer}{count}")
    sleep(1)
print(f"\n{cer}Contador Finalizado com sucesso.")