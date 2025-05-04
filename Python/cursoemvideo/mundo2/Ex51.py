import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Números primos
######## Descrição: "Retorna se o número é primo ou não "

from cursoemvideo.utils import *

n = safe_int_input(f'{choice} Digite um número que seja primo! > ')
if n > 1:
    counter = 0
    print(f'{strTime} Número divisivel por: ', end = '')
    for c in range(1, n + 1):
        # print(c)
        if n % c == 0:
            counter += 1
            print(f'{Fore.GREEN}{c}{Fore.RESET}, ' , end = '')

    if counter == 2:
        print(f' Número primo pois é divisivel apenas por 2 números, ele mesmo e 1')
        True
    else:
        print(f' Número não primo, pois é divisivel por mais de 2 números')
        False