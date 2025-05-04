import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Maioridade
######## Descrição: "Recebe uma lista de idades dadas pelo usuario e verifica a maioridade de todas as pessoas"

from cursoemvideo.utils import *

y = date.today().year
i = []
menor = 0
maior = 0

inputs = safe_int_input(f'{choice} Quantas idades você deseja coletar?')

for inp in range(inputs):
    user_input = safe_int_input(f'{choice}Digite o ano de nascimento da {inp + 1}° pessoa > ')
    i.append(user_input)

for i, value in enumerate(i):
    age = y - value
    if age > 1 and age < 120:
        if age < 18:
            print(f'{err} A {i + 1}° Pessoa da lista é menor de idade! sem drinks!')
            menor += 1
        elif age >= 18:
            print(f'{cer} A {i + 1}° Pessoa da lista é maior de idade! drinks liberados!')
            maior += 1
    else:
        print(f'{err} A {i + 1}° Pessoa da lista tem uma idade inválida!')

print(f'{cer}Ao total temos {Fore.RED}{menor}{Fore.RESET} menores de idade, e {Fore.GREEN}{maior}{Fore.RESET} maiores de idade!')