import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 72 === Número por extenso 
##### Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

from cursoemvideo.utils import *
clear()

num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

numNames = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
            "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
            "dezoito", "dezenove", "vinte")

try:
    n = safe_int_input(f"{choice} Digite um número entre {lg}1{reset} e {lg}20{reset}: ")
except ValueError:
    print(f"{err} Erro, o número digitado não é um número inteiro.")
    quit()

if n > 0 and n < 21:
    print(f"{cer} Você acaba de digitar o número {lg} {n}, ({numNames[n]})")
else:
    print(f"{err} Erro, o número digitado não está entre {lg}1{reset} e {lg}20{reset}.")
    quit()
