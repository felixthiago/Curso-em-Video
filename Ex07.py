######## Nivel: Simples 
######## Exercicio === Números primos
######## Descrição: "Retorna se o número é primo ou não "
####### Módulo finalizado em Março de 2021

from vars import *

try:
    n = int(input(f'{choice} Digite um número que seja primo! > '))
except ValueError:
    print(f'{err} O que foi digitado não se parece com um número!')

if n > 1:
    counter = 0
    print(f'{strTime} Número divisivel por: ', end = '')
    for c in range(1, n + 1):
        if n % c == 0:
            counter += 1
            print(f'{c},' , end = '')


    if counter == 2:
        print(f' Número primo pois é divisivel apenas por 2 números, ele mesmo e 1')
        True
    else:
        print(f' Número não primo, pois é divisivel por mais de 2 números')
        False