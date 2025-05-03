import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio 67 === Jogo par ou ímpar
######## Descrição: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from Exercicios.utils import *
clear()

from random import randint
rn = randint(0, 10)

print(f"""{choice} Jogo Par ou Ímpar
O computador vai pensar em um número e em seguida você deve jogar outro.
caso a soma dos dois números seja par você ganha, caso contrário você perde.
      """)
try:
    n = int(input(f"{choice} > "))
    v = input(f"{choice} Par ou Ímpar? [P/I] > ").strip().upper()[0]
    soma = n + rn
except ValueError:
    print(f"{err} Verifique os valores digitados!!")
    quit()

if v == 'P':
    if soma % 2 == 0:
        print(f"{cer} O número foi: {n + rn}, número par, Você venceu!")
    else:
        print(f"{err} O número foi: {n + rn}, número ímpar, Você perdeu!")
        quit()
elif v == 'I':
    if soma % 3 == 0:
        print(f"{cer} O número foi: {n + rn}, número ímpar, Você venceu!")
    else:
        print(f"{err} O número foi: {n + rn}, número par, Você perdeu!")
        quit()
else:
    print(f"{err} O que foi digitado não se parece com uma opção válida!")
    quit()
