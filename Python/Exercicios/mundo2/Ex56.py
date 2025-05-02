import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Validação de dados
######## Descrição: "Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

from Exercicios.utils import *
clear()

s = input(f"{choice} Digite o seu sexo [M/F]: ").strip().upper()
while s != 'M' and s != 'F':
    s = input(f"{choice}Dados inválidos. Digite o seu sexo [M/F]: ").strip().upper()

if s == 'M':
    print(f"{cer} Sexo Masculino registrado com sucesso!")
elif s == 'F':
    print(f"{cer} Sexo Feminino registrado com sucesso!")