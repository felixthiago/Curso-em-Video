######## Nivel: Simples 
######## Exercicio === Soma de números impares
######## Descrição: "Programa simples onde é somado os números impares apartir de um valor enviado pelo usuário"
####### Módulo finalizado em Março de 2021
from vars import *
clear()


sum = 0
c = 0
c2 = 0

try:
    n = int(input(f'{choice} Até qual número devo somar os impares? > '))
except ValueError:
    print(f'{err} O que você acaba de digitar não se parece com um número...')
    quit()

for count in range(0, n):
    if count % 2 != 0:
        if count % 3 == 0:
            c2 += 1
            c = c + 1
            sum = sum + count
print(f'{cer} A soma de todos os {c2} números impares encontrados é igual a {sum}')