######## Nivel: Simples 
######## Exercicio === Contagem de números pares
######## Descrição: "Programa simples onde é contado os números pares apartir de um valor enviado pelo usuário"
####### Módulo finalizado em Março de 2021

from vars import *
clear()

try:
    n = int(input(f"{strTime}{Fore.LIGHTMAGENTA_EX}Até qual número devo contar os pares? {Fore.RESET}> "))
except ValueError:
    print(f'{err} O que você acaba de digitar não se parece com um número...')
    quit()

l = []



for count in range(0, n):
    if count % 2 == 0:
        l.append(count)
print(f"{cer} Encontrei {len(l)} números pares, aqui estão! >> \n{l}")
