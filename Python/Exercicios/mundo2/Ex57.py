import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Jogo da adivinhação 2.0
######## Descrição: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from Exercicios.utils import *
clear()
from random import randint
r = randint(1, 10)

print(f"{strTime}Acabo de pensar em um número entre 0 e 10, tente adivinhar em três tentativas!")

palpite = int(input(f"{choice}Qual o seu palpite? "))
tentativas = 0
while palpite != r:
    tentativas += 1
    if palpite < r:
        print(f"{strTime} Mais...")
    else:
        print(f"{strTime} Menos...")
    if tentativas == 3:
        print("Você perdeu!")
        break

    palpite = int(input(f"{choice}Qual o seu palpite? "))
    if palpite == r:
        print(f"{cer}Você acertou! O número era {r} e você precisou de {tentativas + 1} tentativas para acertar!")