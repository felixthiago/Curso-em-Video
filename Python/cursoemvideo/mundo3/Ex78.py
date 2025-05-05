import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 83 === Validando expressões matemáticas
##### Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

from cursoemvideo.utils import *
clear()

check = list()
str = safe_str_input(f"{choice}Digite uma expressão numérica com parenteses(EX: (A + B)) > ")
for c in str:
    for letter in c:
        check.append(letter)

if check.count("(") == check.count(")"):
    print(f"{strTime}Sua expressão me parece válida! ")
else:
    print(f"{err}Sua expressão não me parece valida")
