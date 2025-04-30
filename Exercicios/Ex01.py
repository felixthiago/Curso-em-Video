######## Nivel: Simples 
######## Exercicio === Contagem Regressiva
######## Descrição: "Simples Programa onde o usuario manda um número para o programa e o mesmo faz uma contagem regressiva dele"
####### Módulo finalizado em Março de 2021

from time import sleep
from vars import *
clear()

try:
    n = int(input(f'{choice}Até que número devo contar? > '))
except ValueError:
    print(f'{err} O que você acaba de digitar não se parece com um número...')
    quit()

for count in range(n, -1, -1):
    print(f"{cer}{count}")
    sleep(1)
print(f"\n{cer}Contador Finalizado com sucesso.")