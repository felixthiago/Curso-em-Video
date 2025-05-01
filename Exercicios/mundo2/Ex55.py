import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

######## Nivel: Simples 
######## Exercicio === Analisador completo
######## Descrição: "Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."

from Exercicios.utils import *
year = date.today().year

clear()
try:
    inputs_qtd = int(input(f'{choice}Quantas pessoas deseja analisar? > '))
except ValueError:
    print(f'{err} O que foi digitado não se parece com um número! ')
    quit()

p = {}

for inp in range(1, inputs_qtd + 1):
    print(f"""{choice}Analisando {b}{inp}°{reset} pessoa{a}.{b}.{a}.{reset}""")
    nome  = input(f'{strTime} Digite o nome da {b}{inp}°{reset} pessoa > ')

    idade = int(input(f"{strTime} Digite o ano de nascimento de {b}{nome}{reset} > "))
    idade = year - idade
    if idade > 120 or idade < 0:
        print(f'{err} A idade não pode ser maior que 120 anos nem menor que 0!')
        quit()

    sexo  = input(f"{strTime}Digite o sexo da pessoa {a}[{b}M{a}/{b}F{a}]{reset} >").strip().upper()
    if sexo not in 'MF':
        print(f'{err} O sexo digitado não é válido!')
        quit()

    p.update({f'p{inp}': {
    'Nome': f'{nome}',
    'Idade': f"{idade}",
    'Sexo': f'{sexo}'
    }})

print(f"{cer} A média de idade do grupo é de {Fore.BLUE}{round(sum([int(p[f'p{i}']['Idade']) for i in range(1, inputs_qtd + 1)]) / inputs_qtd)}{Fore.RESET} anos")
print(f"{cer} O homem mais velho do grupo é {Fore.BLUE}{max([p[f'p{i}']['Nome'] for i in range(1, inputs_qtd + 1) if p[f'p{i}']['Sexo'] == 'M'])}{Fore.RESET} com {Fore.BLUE}{max([int(p[f'p{i}']['Idade']) for i in range(1, inputs_qtd + 1) if p[f'p{i}']['Sexo'] == 'M'])}{Fore.RESET} anos")
print(f"{cer} O total de mulheres com menos de 20 anos é {Fore.BLUE}{sum([1 for i in range(1, inputs_qtd + 1) if p[f'p{i}']['Sexo'] == 'F' and int(p[f'p{i}']['Idade']) < 20])}{Fore.RESET} e seu nome é {Fore.BLUE}{[p[f'p{i}']['Nome'] for i in range(1, inputs_qtd + 1) if p[f'p{i}']['Sexo'] == 'F' and int(p[f'p{i}']['Idade']) < 20]}{Fore.RESET}")
