######## Nivel: Simples 
######## Exercicio === Soma dos pares
######## Descrição: "Programa simples onde é somado todos os pares encontrados apartir de prompt do usuario"
####### Módulo finalizado em Março de 2021

from vars import *


s = 0 
c = 0
try:
    n = int(input(f"{choice} Até que número devo somar os pares? > "))
except ValueError:
    print(f'{err} O que foi digitado não se parece com um número!')
    quit()

for n in range(1, n):
    if n % 2 == 0:
        c += 1
        s = s + n

print(f'{cer} A soma de todos os {c} números pares encontrados é igual a {s}')