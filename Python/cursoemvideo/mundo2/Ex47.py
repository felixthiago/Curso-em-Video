import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Contagem e soma de números pares (exercicio 47 e 50)
######## Descrição: "Programa simples onde é contado os números pares apartir de um valor enviado pelo usuário"

from cursoemvideo.utils import *
clear()

n = safe_int_input(f"{strTime}{Fore.LIGHTMAGENTA_EX}Até qual número devo contar os pares? {Fore.RESET}> ")

l = []
soma = 0

for count in range(1, n):
    if count % 2 == 0:
        soma += count
        # print(soma)
        l.append(count)
        # print(count)
print(f"{cer} Encontrei {len(l)} números pares, aqui estão! >> \n{l}")
print(f"{cer} A soma entre todos esses {len(l)} números pares é igual a {soma}")