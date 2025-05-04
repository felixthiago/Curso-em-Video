import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Detector de Pallindromos
######## Descrição: "Detecta todos os pallindromos apartir do input do usuario"

from cursoemvideo.utils import *

sentence = safe_str_input(f'{choice} Digite um pallindromo > ')

if sentence == sentence[::-1]:
    print(f"{cer} ({sentence[::-1]}) Essa frase é um pallindromo")