import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 84 + 85 === Matriz em Python
##### Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
### + Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.     
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

from cursoemvideo.utils import *
clear()

matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
c = 0
pares = []
scol = []
maiores = []

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = safe_int_input(f"{choice}Digite um valor para [{l}, {c}] > ")
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matrix[l][c]:^5}]", end = "")
        if matrix[l][c] % 2 == 0:
            pares.append(matrix[l][c])

    scol.append(matrix[c][2])
    maiores.append(matrix[l][1])
    print("")

if len(pares) > 0:
    print(f"{cer}A soma de todos os pares digitados é igual a {sum(pares)}")

print(f"{cer}A soma de todos os valores da terceira coluna > {sum(scol)}")
print(f"{cer}O maior valor da segunda coluna é > {max(maiores)}")
