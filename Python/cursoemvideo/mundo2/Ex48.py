import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Soma de números impares 
######## Descrição: "Programa simples onde é somado os números impares apartir de um valor enviado pelo usuário"

from cursoemvideo.utils import *
clear()

sum = 0
c = 0
c2 = 0

n = safe_int_input(f'{choice} Até qual número devo somar os impares? > ')

for count in range(0, n):
    if count % 2 != 0:
        if count % 3 == 0:
            c2 += 1
            c = c + 1
            sum = sum + count
print(f'{cer} A soma de todos os {c2} números impares encontrados é igual a {sum}')