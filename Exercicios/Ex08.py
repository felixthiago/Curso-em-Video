######## Nivel: Simples 
######## Exercicio === Detector de Pallindromos
######## Descrição: "Detecta todos os pallindromos apartir do input do usuario"
####### Módulo finalizado em Março de 2021


from vars import *

try:
    sentence = str(input(f'{choice} Digite um pallindromo > '))
except ValueError:
    print(f'O que foi digitado não se parece com uma string!')

if sentence == sentence[::-1]:
    print(f"{cer} ({sentence[::-1]}) Essa frase é um pallindromo")